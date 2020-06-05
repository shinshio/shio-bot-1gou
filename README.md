
# shio-bot-1gou

## 覚書

1. LINE Developersでチャンネル設定する。
    - チャネル基本設定
        - チャネルアイコン、名前、説明の設定
        - **チャネルシークレットのメモ**
    - Messaging API 設定
        - QRコードを保存しておく、友達登録する
        - Webhookの利用にチェック<br>"https://<herokuのAPP_NAME>.herokuapp.com/callback"
        - 応答メッセージの編集：個別の受付〜をオフする<br>なんか  herokuだとこの応答が必ず返る？
        - チャネルアクセストークンの発行、メモ
2. heroku 設定
    - ターミナルでheroku設定を行う。

        ```bash
        heroku login
        heroku create <APP_NAME>
        heroku config:set YOUR_CHANNEL_SECRET="LINEのシークレットキー" --app <APP_NAME>
        heroku config:set YOUR_CHANNEL_ACCESS_TOKEN="LINEのアクセストークン" --app <APP_NAME>
        heroku config:add PYTHONPATH=app/reply
        ```

    - gitからherokuにデプロイする

        ```bash
        git init
        git add .
        git commit -m 'some message'
        git remote add heroku <herokuのアプリのアドレス>
        git push heroku master
        ```

## 友だち追加

![友だち追加](./images/line_tomodachi_qrcode.png)
