 ※下で使用手順は記載しておりますが、かなり省略しております。  
 下記の内容で使用手順が理解できなかった場合はぜひ[こちら](https://h4shikan.hatenablog.com/entry/2022/07/18/233825)を参考にしてみてください！！  

# 対象者
こちらのツールはDead by DaylightをPC版（Steam）でプレイしている方が使用できるツールです。  


# ツールの内容
キラーの1日の戦績を自動でツイートしてくれるツールです。  
ナースでブリンク攻撃をした回数やブライトで突進攻撃を当てた回数など。  
（※[DbDstats](https://dbd.tricky.lol/)で見られるキラーの戦績に限る。）

![スクリーンショット 2022-07-18 16 45 30](https://user-images.githubusercontent.com/109508477/179466294-657521fe-55e6-4f20-b5c7-253cf4d2b9be.png)


# 前提環境
ツールはPythonで作成しているため、Pythonを実行できる環境が必須です。
[Python = 3.6~]  
## 必要なライブラリ  
・BeautifulSoup4  
・Tweepy  

# 使用手順  
## 1.任意のフォルダにファイルをダウンロード  
右上にある黄緑色のボタンを押して、「Download ZIP」でファイルをダウンロード。  
ダウンロードしたファイルを任意のフォルダに解凍。  
## 2.ライブラリをインストール  
```
cd "ダウンロードしたフォルダのパス"
pip install -r requirements.txt
```
## 3.TwitterのAPIおよびSteam64IDを取得  
下のURLから必要な情報を取得して、メモしておく。  
  ・[TwitterのAPI取得方法](https://di-acc2.com/system/rpa/9688/)  
  ・[Steam64IDの取得方法](https://volx.jp/steam-id-steamid64-check)    
## 4.input_info.pyに必要情報を書き込む（合計8箇所）   
![スクリーンショット 2022-07-18 21 33 09](https://user-images.githubusercontent.com/109508477/179512008-992e0687-0ebb-4b53-be31-d33ce6eed908.png)


## 5. AutoTweetStats.pyを実行  
```
cd "ダウンロードしたフォルダのパス"
python AutoTweetStats.py
```

（※個人で作ったツールなので上手く動作しない可能性があります。何かあれば気軽に、[@HashikaN44](https://twitter.com/HashikaN44)までDMください！！）
