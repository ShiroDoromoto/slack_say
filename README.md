# はじめに

ターミナルを開く。
cdでslack_sayのディレクトリに移動する。

./intall.sh
を実行してください。

# 初期設定
このページから、xoxp-で始まるトークンを取得してください。
https://api.slack.com/custom-integrations/legacy-tokens

# 使う

ターミナルを開く。
cdでslack_sayのディレクトリに移動する。

そこで、lsを叩くと、app.pyがあるはず。

そして、これを実行
python app.py "xoxp-xxxxxxxxxxxx-xxxxxxxxxxx-xxxxxxxxxxx-xxxxxxxxxxxxxxxxxxxxxxxxxxx"

この状態で、Slackにメッセージがあったら、発話があるはず。
