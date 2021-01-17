#!/usr/bin/python3
#!python3.7
# -*- coding: utf-8 -*-
import os,sys
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import csv
import pandas as pd

def categorize_for_person(row):
    if row[6] == '共通':
        common_carfare += int(row[3])
    elif row[6] == 'ともこ':
        tomoko_carfare += int(row[3])
    elif row[6] == 'るな':
        luna_carfare += int(row[3])
    else:
        other_carfare += int(row[3])

def analyze_data(incsv):
    common_food = 0
    tomoko_food = 0
    luna_food = 0
    eat_out = 0
    common_livingware = 0
    tomoko_livingware = 0
    luna_livingware = 0
    other_livingware = 0
    common_housing = 0
    tomoko_housing = 0
    luna_housing = 0
    other_housing = 0
    common_carfare = 0
    tomoko_carfare = 0
    luna_carfare = 0
    other_carfare = 0
    common_phone = 0
    tomoko_phone = 0
    luna_phone = 0
    other_phone = 0
    common_energy = 0
    tomoko_energy = 0
    luna_energy = 0
    other_energy = 0
    common_edu = 0
    tomoko_edu = 0
    luna_edu = 0
    other_edu = 0
    common_hobby = 0
    tomoko_hobby = 0
    luna_hobby = 0
    yukimaru_hobby = 0
    ham_hobby = 0
    other_hobby = 0
    common_clothing = 0
    tomoko_clothing = 0
    luna_clothing = 0
    other_clothing = 0
    common_med = 0
    tomoko_med = 0
    luna_med = 0
    other_med = 0
    common_gift = 0
    tomoko_gift = 0
    luna_gift = 0
    other_gift = 0
    common_social = 0
    tomoko_social = 0
    luna_social = 0
    other_social = 0
    other_cost = 0
    all_cost = 0
    with open(incsv) as rf:
        reader = csv.reader(rf)
        for row in reader:
            if row[1] == '支出':
                all_cost += int(row[2])
                if row[3] == '食費':
                    if row[7] == '外食':
                        eat_out += int(row[2])
#                    else:
#                        eat_out += int(row[2])
                    elif row[6] == '共通':
                        common_food += int(row[2])
                    elif row[6] == 'ともこ':
                        tomoko_food += int(row[2])
                    elif row[6] == 'るな':
                        luna_food += int(row[2])
                    else:
                        eat_out += int(row[2])

                elif row[3] == '生活雑費':
                    if row[6] == '共通':
                        common_livingware += int(row[2])
                    elif row[6] == 'ともこ':
                        tomoko_livingware += int(row[2])
                    elif row[6] == 'るな':
                        luna_livingware += int(row[2])
                    else:
                        other_livingware += int(row[2])
                elif row[3] == '住居費':
                    if row[6] == '共通':
                        common_housing += int(row[2])
                    elif row[6] == 'ともこ':
                        tomoko_housing += int(row[2])
                    elif row[6] == 'るな':
                        luna_housing += int(row[2])
                    else:
                        other_housing += int(row[2])
                elif row[3] == '交通費':
                    if row[6] == '共通':
                        common_carfare += int(row[2])
                    elif row[6] == 'ともこ':
                        tomoko_carfare += int(row[2])
                    elif row[6] == 'るな':
                        luna_carfare += int(row[2])
                    else:
                        other_carfare += int(row[2])
                elif row[3] == '通信費':
                    if row[6] == '共通':
                        common_phone += int(row[2])
                    elif row[6] == 'ともこ':
                        tomoko_phone += int(row[2])
                    elif row[6] == 'るな':
                        luna_phone += int(row[2])
                    else:
                        other_phone += int(row[2])
                elif row[3] == '光熱費':
                    if row[6] == '共通':
                        common_energy += int(row[2])
                    elif row[6] == 'ともこ':
                        tomoko_energy += int(row[2])
                    elif row[6] == 'るな':
                        luna_energy += int(row[2])
                    else:
                        other_energy += int(row[2])
                elif row[3] == '教育教養費':
                    if row[6] == '共通':
                        common_edu += int(row[2])
                    elif row[6] == 'ともこ':
                        tomoko_edu += int(row[2])
                    elif row[6] == 'るな':
                        luna_edu += int(row[2])
                    else:
                        other_edu += int(row[2])
                elif row[3] == '娯楽費':
                    if row[6] == '共通':
                        common_hobby += int(row[2])
                    elif row[6] == 'ともこ':
                        tomoko_hobby += int(row[2])
                    elif row[6] == 'るな':
                        luna_hobby += int(row[2])
                    elif row[6] == 'ゆきまる':
                        yukimaru_hobby += int(row[2])
                    elif row[6] == 'ハム':
                        ham_hobby += int(row[2])
                    else:
                        other_hobby += int(row[2])
                elif row[3] == '被服費':
                    if row[6] == '共通':
                        common_clothing += int(row[2])
                    elif row[6] == 'ともこ':
                        tomoko_clothing += int(row[2])
                    elif row[6] == 'るな':
                        luna_clothing += int(row[2])
                    else:
                        other_clothing += int(row[2])
                elif row[3] == '医療費':
                    if row[6] == '共通':
                        common_med += int(row[2])
                    elif row[6] == 'ともこ':
                        tomoko_med += int(row[2])
                    elif row[6] == 'るな':
                        luna_med += int(row[2])
                    else:
                        other_med += int(row[2])
                elif row[3] == 'ギフト・プレゼント':
                    if row[6] == '共通':
                        common_gift += int(row[2])
                    elif row[6] == 'ともこ':
                        tomoko_gift += int(row[2])
                    elif row[6] == 'るな':
                        luna_gift += int(row[2])
                    else:
                        other_gift += int(row[2])
                elif row[3] == '交際費':
                    if row[6] == '共通':
                        common_social += int(row[2])
                    elif row[6] == 'ともこ':
                        tomoko_social += int(row[2])
                    elif row[6] == 'るな':
                        luna_social += int(row[2])
                    else:
                        other_social += int(row[2])
                else:
                    other_cost += int(row[2])
            else:
                pass
    print(all_cost)
    common_list = [common_food, common_livingware, common_housing,\
                   common_carfare, common_phone, common_energy,\
                   common_edu, common_hobby, common_clothing, common_med,\
                   common_gift, common_social, 0, "=SUM(B2:N2)",\
                   ".", "=O2*0.4", "=O2*0.6"]
    tomoko_list = [tomoko_food, tomoko_livingware, tomoko_housing,\
                   tomoko_carfare, tomoko_phone, tomoko_energy,\
                   tomoko_edu, tomoko_hobby, tomoko_clothing, tomoko_med,\
                   tomoko_gift, tomoko_social, 0, "=SUM(B3:N3)",\
                   ".", ".", "=O3"]
    luna_list = [luna_food, luna_livingware, luna_housing,\
                 luna_carfare, luna_phone, luna_energy,\
                 luna_edu, luna_hobby, luna_clothing, luna_med,\
                 luna_gift, luna_social, 0, "=SUM(B4:N4)",\
                 ".", "=O4", "."]
    yukimaru_list = [0, 0, 0, 0, 0, 0, 0, yukimaru_hobby,\
                     0, 0, 0, 0, 0, "=SUM(B5:N5)",\
                     ".", "=O5*0.5", "=O5*0.5"]
    ham_list = [0, 0, 0, 0, 0, 0, 0, ham_hobby,\
                0, 0, 0, 0, 0, "=SUM(B6:N6)",\
                ".", ".", "=O6"]
    other_list = [eat_out, other_livingware, other_housing,\
                  other_carfare, other_phone, other_energy,\
                  other_edu, other_hobby, other_clothing, other_med,\
                  other_gift, other_social, other_cost, "=SUM(B7:N7)",\
                  ".", ".", "=O7"]
    sum_list = ['=SUM(B2:B7)', '=SUM(C2:C7)', '=SUM(D2:D7)', '=SUM(E2:E7)', \
                '=SUM(F2:F7)', '=SUM(G2:G7)', '=SUM(H2:H7)', '=SUM(I2:I7)', \
                '=SUM(J2:J7)', '=SUM(K2:K7)', '=SUM(L2:L7)', '=SUM(M2:M7)', \
                '=SUM(N2:N7)', '=SUM(O2:O7)', '.', '=SUM(Q2:Q7)', '=SUM(R2:R7)']
    data_frame_list = [common_list, tomoko_list, luna_list, \
                       yukimaru_list, ham_list, other_list, sum_list]

    col_list = ['食費', '生活雑貨', '住居費', '交通費', '通信費', '光熱費',\
                '教育教養費', '娯楽費', '被服費', '医療費', 'ギフト', '交際費', 'その他', '合計',\
                '.', 'るな', 'ともこ']
    index_list = ['共通', 'ともこ', 'るな', 'ゆきまる', 'ハム', 'その他', '合計']
    # 出力ファイル名の取得
    outxlsx = os.path.splitext(incsv)[0] + '_done.xlsx'
    df = pd.DataFrame(data_frame_list, index=index_list, columns=col_list)
#    df.to_excel(outxlsx, sheet_name='家計簿')
    with pd.ExcelWriter(outxlsx) as wf:
        df.to_excel(wf, sheet_name='sheet1')

    return outxlsx
 #   with open(outcspy
 # v, 'w') as wf:
 #       writer = csv.writer(f)
 #       writer.writerow(['#', '食費', '生活雑貨', '住居費', '交通費', '通信費', '光熱費',\
 #                        '教育教養費', '娯楽費', '被服費', '医療費', 'ギフト', '交際費', 'その他'])
 #       writer.writerow(['a', 'b', 'c'])


# 参照ボタンのイベント
# button1クリック時の処理
def button1_clicked():
    fTyp = [("","*")]
    iDir = os.path.abspath(os.path.dirname(__file__))
    filepath = filedialog.askopenfilename(filetypes = fTyp,initialdir = iDir)
    file1.set(filepath)

# button2クリック時の処理
def button2_clicked():
    incsv = file1.get()
    outxlsx = analyze_data(incsv)
    messagebox.showinfo('正常終了', u'出力ファイルは\n' + outxlsx)

if __name__ == '__main__':
    # rootの作成
    root = Tk()
    root.title('FileReference Tool')
    root.resizable(False, False)

    # Frame1の作成
    frame1 = ttk.Frame(root, padding=10)
    frame1.grid()

    # 参照ボタンの作成
    button1 = ttk.Button(root, text=u'参照', command=button1_clicked)
    button1.grid(row=0, column=3)

    # ラベルの作成
    # 「ファイル」ラベルの作成
    s = StringVar()
    s.set('ファイル>>')
    label1 = ttk.Label(frame1, textvariable=s)
    label1.grid(row=0, column=0)

    # 参照ファイルパス表示ラベルの作成
    file1 = StringVar()
    file1_entry = ttk.Entry(frame1, textvariable=file1, width=50)
    file1_entry.grid(row=0, column=2)

    # Frame2の作成
    frame2 = ttk.Frame(root, padding=(0,5))
    frame2.grid(row=1)

    # Startボタンの作成
    button2 = ttk.Button(frame2, text='Start', command=button2_clicked)
    button2.pack(side=LEFT)

    # Cancelボタンの作成
    button3 = ttk.Button(frame2, text='Cancel', command=quit)
    button3.pack(side=LEFT)

    root.mainloop()
