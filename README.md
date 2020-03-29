# pdf_viewer

どうも、pdf_viwewer (仮) をダウンロードいただきありがとうございます。

## 環境

- 以下の環境を整備してください
  - pipenv
    - https://qiita.com/anvinon/items/5d9c128ef8b65b866dfe

  - pdfjs
    - wgetやらでファイルを取得してこのテキストと同じ階層に解凍
    - https://qiita.com/kroton/items/cc38dbcfc4a6fefcd2c0

## 使い方

- pdfjs/web/ に読みたい論文を設置すればオーケーです
- make_html.py でファイルの状態を反映します
- ajax 通信には対応してないので途中でファイル構成が変わっても対応できません
- activate_server.py でサーバーを立ち上げます
- 表示された url にアクセスすればディレクトリを確認できます
- 現在、入れ子のディレクトリの中身は参照できません <- 対応しました!
