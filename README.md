# WhiteStoriesBot
Discord上で白物語をプレイするためのBotです。

## 1.使うための準備
このBotを使う準備として、Botの作成、Python環境の構築が必要になります。
順番にやっていきましょう。
といっても外部サイトの参照がほとんどですが。

### Botの作成
まずはBotを用意しましょう。
こちらのサイト↓で詳しく解説されています。
https://dev.classmethod.jp/articles/discord-bot-by-discordpy/
サーバへの追加は、不安でなければ初めからご使用されるサーバへの追加としてもよいかと思います。

### Python環境の構築
Python公式サイト↓にアクセスし、Python3のインストーラをダウンロードします。
https://www.python.org/downloads/

私の環境がバージョン3.9.12ですので、近いバージョンを使えば確実に動くはずです。たぶん。

Windowでコマンドプロンプトを使用する場合は以下のコマンドを、
```
py -3 -m pip install -U discord.py
```

PowerShellであったりWSLを使う場合は以下のコマンドを使用してください。
```
python3 -m pip install -U discord.py
```
Mac環境はカバーできてないですすみません。
Pythonなので動くとは思います。

## 実際に動かしてみる
ここまで来たら準備は完了です。
WhiteStoriesBot.pyをダウンロードして、実際に動かしてみましょう。
シェルを起動して、WhiteStoriesBotを置くためのフォルダを作ります。
詳しくない方はUserディレクトリ直下などに以下のコマンドでWhiteStoriesBotフォルダを作ることをお勧めします。
(1行づつ実行してくださいね）
```
mkdir WhiteStoriesBot
cd WhiteStoriesBot
```

gitを使ってる方は適当にクローンしておいてください（そもそもgit使ってる人ならこれ読まなくてもよい気がする）。
git環境をお持ちでない方は、zipをダウンロードして解凍して、先ほど作ったフォルダにDiceBot.pyを配置しましょう。

配置ができたら、シェル上で以下のコマンドを入力します。
```
python3 WhiteStoriesBot.py
```
Botを設置したサーバでBotが起動しますと、シェル上に「ログインしました」と表示されます。
これで起動完了です。
コマンドは以下の通り。
```
.ws n  //新しいゲームの開始
.ws d  //ダイスを振る
.ws e  //ゲームを終了する（リセットする）
```
よくよく考えたら名前以外をリセットするコマンドが必要ですね。
そのうち実装します。
