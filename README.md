# 対象者
こちらはデッドバイデイライトのPC版（Steam）でプレイしている方のみが使用できるツールとなっています。  


# ツールの内容
自動で1日の戦績をツイートしてくれるツールです。  

![スクリーンショット 2022-07-18 16 45 30](https://user-images.githubusercontent.com/109508477/179466294-657521fe-55e6-4f20-b5c7-253cf4d2b9be.png)


# 前提環境
ツールはPythonで作成しているため、Pythonを実行できる環境が必須です。
[Python = 3.6~]  
## 必要なライブラリ  
・BeautifulSoup4  
・Tweepy  
（※コマンドプロントで下記のコマンドと入力すると一括インストールされます。）  
```
cd "ダウンロードしたフォルダのパス"
pip install -r requirements.txt
```

# 使用方法
1.TwitterのAPIおよびSteam64IDを取得  
  ・[TwitterのAPI取得方法](https://di-acc2.com/system/rpa/9688/)  
  ・[Steam64IDの取得方法](https://volx.jp/steam-id-steamid64-check)    
2.input_info.pyの中にTwitterのAPIやDbDの情報を入力    
3. AutoTweetStats.pyを実行  
```
cd "ダウンロードしたフォルダのパス"
python AutoTweetStats.py
```

（※個人で作ったツールなので上手く動作しない可能性があります。何かあれば気軽に、[@HashikaN44](https://twitter.com/HashikaN44)までDMください！！）
