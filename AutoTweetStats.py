import tweepy
from time import sleep
import re
import requests
from bs4 import BeautifulSoup
import datetime
import input_info as ii

def checkURL(url):
    flag = True
    try:
        response = requests.get(url)
        response.close()
    except:
        print ("プロフィールが見つかりませんでした。Steam64IDが正しくないか、プロフィールの公開設定が正しくありません。")
        flag = False
    return flag
        
def generateURL(userID, killer_idx):
    pageURL = []
    ranking = []
    status = []

    # ユーザに情報を入力させる情報
    userSteam64ID = userID
    killerSelect = killer_idx

    # キラー分岐
    if killerSelect == "1" or killerSelect == "１":
        ranking = ["BeartrapCatches"]
        Killer = "トラッパー"
        status = ["罠にかけた回数"]
    elif killerSelect == "2" or killerSelect == "２":
        ranking = ["UncloakAttacks"]
        Killer = "レイス"
        status = ["透明化解除後に負傷させた回数"]
    elif killerSelect == "3" or killerSelect == "３":
        ranking = ["ChainsawHits"]
        Killer = "ヒルビリー"
        status = ["チェーンソーを当てた回数"]
    elif killerSelect == "4" or killerSelect == "４":
        ranking = ["BlinkAttacks"]
        Killer = "ナース"
        status = ["ブリンク攻撃した回数"]
    elif killerSelect == "5" or killerSelect == "５":
        ranking = ["PhantasmsTriggered"]
        Killer = "ハグ"
        status = ["罠を発動させた回数"]
    elif killerSelect == "6" or killerSelect == "６":
        ranking = ["EvilWithinTierUp"]
        Killer = "シェイプ"
        status = ["内なる邪悪のTierをあげた回数"]
    elif killerSelect == "7" or killerSelect == "７":
        ranking = ["Shocked"]
        Killer = "ドクター"
        status = ["ショックセラピーを当てた回数"]
    elif killerSelect == "8" or killerSelect == "８":
        ranking = ["HatchetsThrown","survivorsdowned_hatchets"]
        Killer = "ハントレス"
        status = ["手斧を当てた回数","24m以上からのダウン数"]
    elif killerSelect == "9" or killerSelect == "９":
        ranking = ["DreamState"]
        Killer = "ナイトメア"
        status = ["夢に引き込んだ回数"]
    elif killerSelect == "10" or killerSelect == "１０":
        ranking = ["RBTsPlaced"]
        Killer = "ピッグ"
        status = ["逆トラバサミを設置した回数"]
    elif killerSelect == "11" or killerSelect == "１１":
        ranking = ["CagesofAtonement"]
        Killer = "エクセキューショナー"
        status = ["贖罪の檻に送った回数"]
    elif killerSelect == "12" or killerSelect == "１２":
        ranking = ["LethalRushHits"]
        Killer = "ブライト"
        status = ["突進攻撃を当てた回数"]
    elif killerSelect == "13" or killerSelect == "１３":
        ranking = ["Lacerations"]
        Killer = "トリックスター"
        status = ["ナイフで負傷させた回数"]
    elif killerSelect == "14" or killerSelect == "１４":
        ranking = ["PossessedChains"]
        Killer = "セノバイト"
        status = ["鎖を当てた回数"]
    elif killerSelect == "15" or killerSelect == "１５":
        ranking = ["survivorsdowned_chainsaw"]
        Killer = "カニバル"
        status = ["チェーンソーでダウンさせた回数"]
    elif killerSelect == "16" or killerSelect == "１６":
        ranking = ["survivorsdowned_intoxicated"]
        Killer = "クラウン"
        status = ["サバイバーが中毒時にダウンさせた回数"]
    elif killerSelect == "17" or killerSelect == "１７":
        ranking = ["survivorsdowned_haunting"]
        Killer = "スピリット"
        status = ["山岡の祟り使用後にサバイバーをダウンさせた回数"]
    elif killerSelect == "18" or killerSelect == "１８":
        ranking = ["survivorsdowned_deepwound"]
        Killer = "リージョン"
        status = ["深手中にサバイバーをダウンさせた回数"]
    elif killerSelect == "19" or killerSelect == "１９":
        ranking = ["survivorsdowned_maxsickness"]
        Killer = "プレイグ"
        status = ["感染中にサバイバーをダウンさせた回数"]
    elif killerSelect == "20" or killerSelect == "２０":
        ranking = ["survivorsdowned_marked"]
        Killer = "ゴーストフェイス"
        status = ["マーキング中のサバイバーをダウンさせた回数"]
    elif killerSelect == "21" or killerSelect == "２１":
        ranking = ["survivorsdowned_shred"]
        Killer = "デモゴルゴン"
        status = ["シュレッドでサバイバーをダウンさせた回数"]
    elif killerSelect == "22" or killerSelect == "２２":
        ranking = ["survivorsdowned_bloodfury"]
        Killer = "鬼"
        status = ["鬼の一撃でサバイバーをダウンさせた回数"]
    elif killerSelect == "23" or killerSelect == "２３":
        ranking = ["survivorsdowned_speared"]
        Killer = "デススリンガー"
        status = ["銛を当ててサバイバーをダウンさせた回数"]
    elif killerSelect == "24" or killerSelect == "２４":
        ranking = ["survivorsdowned_victor"]
        Killer = "ツインズ"
        status = ["ヴィクトルでサバイバーをダウンさせた回数"]
    elif killerSelect == "25" or killerSelect == "２５":
        ranking = ["survivorsdowned_contaminated"]
        Killer = "ネメシス"
        status = ["触手攻撃でサバイバーをダウンさせた回数"]
    elif killerSelect == "26" or killerSelect == "２６":
        ranking = ["survivorsdowned_direcrows"]
        Killer = "アーティスト"
        status = ["不吉なカラスでサバイバーをダウンさせた回数"]
    elif killerSelect == "27" or killerSelect == "２７":
        ranking = ["condemned"]
        Killer = "怨霊"
        status = ["呪いを付与した回数"]
    elif killerSelect == "27" or killerSelect == "２８":
        ranking = ["survivorsdowned_nightfall"]
        Killer = "アーティスト"
        status = ["日没中にサバイバーをダウンさせた回数"]
    else:
        ranking = [""]
        Killer = ""
        status = [""]
    
    for index in range(len(ranking)):
        # URLを生成する 
        pageURL.append(f"https://dbd.tricky.lol/api/leaderboardposition?steamid={userSteam64ID}&stat={ranking[index]}")

    return killerSelect,status,pageURL

# クライアント関数を作成
def ClientInfo():
    client = tweepy.Client(bearer_token    = BEARER_TOKEN,
                           consumer_key    = API_KEY,
                           consumer_secret = API_SECRET,
                           access_token    = ACCESS_TOKEN,
                           access_token_secret = ACCESS_TOKEN_SECRET,
                          )
    return client

def AutoTweet(message):
    tweet = ClientInfo().create_tweet(text=message)
    return tweet

if __name__ == '__main__':
    # 00 事前情報（API情報やゲーム情報）を記入
    BEARER_TOKEN        = ii.BEARER_TOKEN
    API_KEY             = ii.API_KEY
    API_SECRET          = ii.API_SECRET 
    ACCESS_TOKEN        = ii.ACCESS_TOKEN
    ACCESS_TOKEN_SECRET = ii.ACCESS_TOKEN_SECRET

    KILLER = ii.KILLER
    USER_ID = ii.USER_ID
    TEMPLATE = ii.TEMPLATE

    two_stats_killer_idx = ["8"]
    old_message = ""
    old_stats1 = 0
    old_stats2 = 0

    while True:
        # 01 戦績の取得
        val = []
        pos = []
        URL_checker = []
        killer_idx,status,pageURL = generateURL(USER_ID, KILLER)

        for url in pageURL: # URLが存在するかを確認
            URL_checker.append(checkURL(url))

        for statsURL in pageURL: # APIを用いて戦績を取得
            response = requests.get(statsURL)
            html_text = str(BeautifulSoup(response.content,"html.parser"))
            if not html_text == "too many requests": # 正常処理
                response.close()
                value = re.sub(r"\D", "", html_text.split(",")[1])
                position = re.sub(r"\D", "", html_text.split(",")[2])

                val.append(value)
                pos.append(position)
                sleep(5)
            else: # 例外処理
                print("[Error]: しばらく時間をおいてから再度実行してください。")
                exit()
        if killer_idx in two_stats_killer_idx:
            message = f'{status[0]}: {val[0]}回（{pos[0]}位）{status[1]}: {val[1]}回（{pos[1]}位）'
        else:
            message = f'{status[0]}: {val[0]}回（{pos[0]}位）'

        # 02 ツイートの作成　＆　ログ出力
        if old_message == "": # 初期設定
            old_message = message
            old_stats1 = int(val[0])
            if killer_idx in two_stats_killer_idx: 
                old_stats2 = int(val[1])
            print(f"[{datetime.datetime.now().time().strftime('%X')}][Log]: Data set is complete.")
        
        elif not old_message == message: # 更新処理
            print(f"[{datetime.datetime.now().time().strftime('%X')}][Log]:Entry Tweet mode.")
            old_message = message
            new_stats1 = int(val[0]) - old_stats1
            if killer_idx in two_stats_killer_idx: 
                new_stats2 = int(val[1]) - old_stats2
            if killer_idx in two_stats_killer_idx: 
                new_message = f'【{TEMPLATE}】\n{status[0]}: {new_stats1}回\n{status[1]}: {new_stats2}回'
            else:
                new_message = f'【{TEMPLATE}】\n{status[0]}: {new_stats1}回'
            print(f"[{datetime.datetime.now().time().strftime('%X')}][Tweet]: {new_message}")
            AutoTweet(new_message)
            old_stats1 = int(val[0])
            if killer_idx in two_stats_killer_idx: 
                old_stats2 = int(val[1])
            print(f"[{datetime.datetime.now().time().strftime('%X')}][Log]: Your tweet has been sent, stand by for one day.")
            sleep(ii.AFTER_TWEET_TIME)
        
        else: # 待機処理
            print(f"[{datetime.datetime.now().time().strftime('%X')}][Log]: The same message was created. Therefore, we wait for one hour.")
            print(f"[{datetime.datetime.now().time().strftime('%X')}][Message]: {message}")
            sleep(ii.STOP_TIME)
 