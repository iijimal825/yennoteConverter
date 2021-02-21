# yennoteConverter

Windows 10の家計簿アプリ「yen-note」から出力された月間収支ファイル（CSV形式）を取り込み、収支のカテゴリ・利用者ごとに区分し、Excel形式で出力する。

Convert CSV (by yen-note for Windows 10) into EXCEL.

## 動作環境

OS: Ubuntu 18.04 (WSL)
ブラウザ: Google Chrome 88.0.4324.150
開発言語: Python 3系
    Django==3.1.6
    django-cleanup==5.1.0
    django-pandas==0.6.4

## 起動方法

```sh
$ git clone git@github.com:iijimal825/yennoteConverter.git
$ cd ./yennoteConverter
# モデルの作成
$ python manage.py makemigrations app
$ python manage.py migrate
# スーパーユーザーの作成
$ python manage.py createsuperuser
# アプリケーションの起動
$ python manage.py runserver
```

起動したら、http://localhost:8000/ にアクセスする。