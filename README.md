# はじめに

ターミナルを開く。
cdでslack_sayのディレクトリに移動する。

## homebrewのインストール

```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

## pyenvのインストール

```
brew install pyenv
```

## 環境変数にPYENV_ROOTを反映

```
echo 'export PYENV_ROOT=/usr/local/var/pyenv' >> ~/.bash_profile
echo 'if which pyenv > /dev/null; then eval "$(pyenv init -)"; fi' >> ~/.bash_profile
. ~/.bash_profile
```

## python3系をインストール

```
pyenv install 3.6.5
```

## ローカルに反映

```
pyenv local 3.6.5
python -V
```

## slackclientをインストール

```
pip install slackclient --user
```

# Slackからトークンを取得して設定

```
このページから、xoxp-で始まるトークンを取得してください。
https://api.slack.com/custom-integrations/legacy-tokens
```

# 使う

```
python app.py "xoxp-xxxxxxxxxxxx-xxxxxxxxxxx-xxxxxxxxxxx-xxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

チャネルを限定する場合

```
python app.py "xoxp-xxxxxxxxxxxx-xxxxxxxxxxx-xxxxxxxxxxx-xxxxxxxxxxxxxxxxxxxxxxxxxxx" "channel1,channel2"
```

キーワードを限定する場合

```
python app.py "xoxp-xxxxxxxxxxxx-xxxxxxxxxxx-xxxxxxxxxxx-xxxxxxxxxxxxxxxxxxxxxxxxxxx" "" "hogehoge,piyopiyo"
```

この状態で、Slackにメッセージがあったら、発話があるはず。
