#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
#import tkinter as tk
#from tkinter import ttk
#from tkinter import filedialog
#from tkinter import messagebox
import pandas as pd
from django.core.files import File
from django.conf import settings
from .models import FileUpload


class Analyze:
    def __init__(self):
        self.cat_list = [
            '食費', '生活雑費', '住居費', '交通費', '通信費', '光熱費',
            '教育教養費', '娯楽費', '被服費', '医療費',
            'ギフト・プレゼント', '交際費', 'その他'
        ]
        self.user_list = ['共通', 'ともこ', 'るな', 'ゆきまる', 'ハム', 'その他']
        self.ratio_tmk_list = [
            0.6, 1, 0, 0.5, 1, 1
        ]
        self.payer_dict = {
            'ともこ': [0.6, 1, 0, 0.5, 1, 1],
            'るな': [0.4, 0, 1, 0.5, 0, 0]
        }

    def read_csv(self, incsv):
        # yen-note csv を DataFrame に変換する
        try:
            # utf-8に対応
            df_csv = pd.read_csv(incsv)
        except UnicodeDecodeError:
            # cp932に対応
            df_csv = pd.read_csv(incsv, encoding='cp932')
        # 支出のみ抽出する
        df_expence = df_csv.query('金額 < 0')
        return df_expence

    def sum_normal(self, df):
        sum_list = []
        # user ごとの合計を算出する
        for user in self.user_list:
            df_user = df[df['利用者'].str.contains(user)]
            cost = df_user['金額'].sum()
            sum_list.append(cost)
        # 除外された行の合計をその他に合算する
        df_other = df[~df['利用者'].isin(self.user_list)]
        sum_list[-1] += df_other['金額'].sum()
        return sum_list

    def exclude_eat_out(self, df):
        # 外食はその他に加算する
        cost = df[df['ショップ'].str.contains('外食')]['金額'].sum()
        df_after = df[~df['ショップ'].isin(['外食'])]
        return cost, df_after

    def edit_sum_row(self, row_len, col_len):
        # アルファベット大文字の list を取得
        abc_list = [chr(i) for i in range(65, 65+26)]
        # SUM 関数を作成
        sum_list = []
        for i in range(col_len):
            col = abc_list[i+1]
            str_sum = '=SUM({0}{1}:{0}{2})'.format(col, 2, row_len+1)
            sum_list.append(str_sum)
        return sum_list

    def edit_ratio_row(self, row_len, col_len, ratio_list):
        # アルファベット大文字の list を取得
        abc_list = [chr(i) for i in range(65, 65+26)]
        # 支払い割合行を作成
        sum_list = []
        for i, ratio in enumerate(ratio_list):
            col = abc_list[i+1]
            str_sum = '={0}{1}*{2}'.format(col, row_len+1, ratio)
            sum_list.append(str_sum)
        return sum_list

    def edit_sum_col(self, row_len, col_len):
        # アルファベット大文字の list を取得
        abc_list = [chr(i) for i in range(65, 65+26)]
        col1 = abc_list[1]
        col2 = abc_list[col_len]
        # SUM 関数を作成
        sum_list = []
        for i in range(row_len):
            str_sum = '=SUM({0}{2}:{1}{2})'.format(col1, col2, i+2)
            sum_list.append(str_sum)
        return sum_list

    def run(self, incsv, pk):
        df = self.read_csv(incsv)
        # カテゴリごとに集計
        self.sum_dict = {}
        self.output_list = []
        for category in self.cat_list:
            # 初期化する
            sum_list = []
            # 該当 category DataFrame を作成する
            df_cat = df[df['カテゴリ'].str.contains(category)]
            if category == '食費':
                cost_eat_out, df_cat = self.exclude_eat_out(df_cat)
                sum_list = self.sum_normal(df_cat)
                sum_list[-1] += cost_eat_out
            elif category == 'その他':
                for i in range(len(self.user_list)):
                    sum_list.append(0)
                sum_list[-1] += df_cat['金額'].sum()
            else:
                sum_list = self.sum_normal(df_cat)
            self.sum_dict[category] = sum_list
            self.output_list.append(sum_list)
        # 合計行を作成する
        sum_list = self.edit_sum_row(len(self.cat_list), len(self.user_list))
        self.output_list.append(sum_list)
        self.cat_list.append('合計')
        # 支払者行を作成する
        sum_row_num = len(self.cat_list)
        for i, (payer, ratio_list) in enumerate(self.payer_dict.items()):
            sum_list = self.edit_ratio_row(sum_row_num, len(self.user_list), ratio_list)
            self.output_list.append(sum_list)
            self.cat_list.append(payer)
        # 合計列を作成する
        row_sum_list = self.edit_sum_col(len(self.cat_list), len(self.user_list))
        for i, cat_sum_list in enumerate(self.output_list):
            cat_sum_list.append(row_sum_list[i])
        self.user_list.append('合計')
        # 解析後DataFrameを作成
        df = pd.DataFrame(self.output_list, index=self.cat_list, columns=self.user_list)
        
        # 出力ファイルの作成
        # mediaルートとFileUploadモデルに渡す相対パス
        outxlsx = os.path.join('xlsx', os.path.splitext(os.path.basename(incsv))[0] + '_done.xlsx')
        # ファイルを書き込む際に渡す絶対パス
        media_outxlsx = os.path.join(settings.MEDIA_ROOT, outxlsx)
        # Data Frame の書き込み
        with pd.ExcelWriter(media_outxlsx) as wf:
            df.to_excel(wf, sheet_name='sheet1')
        # DB の更新
        rec = FileUpload.objects.get(id=pk)
        rec.analyzed_file = outxlsx
        rec.save()
        return df
