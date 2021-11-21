### 設定手順(Windows版)

1. Python3をインストールする

2. repositoryをcloneする　`git clone <url>`

3. 仮想環境構築する `python -m venv venv`

4. 仮想環境実行する `venv\Scripts\activate`

5. パッケージをインストールする `pip install -r requirements.txt`

6. DBテーブルをマイグレーションする `python manage.py migrate`

7. Djangoサーバを実行する `python manage.py runserver`
