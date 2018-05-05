import os
import tweepy
from datetime import timedelta

CK=os.environ['CONSUMER_KEY']
CS=os.environ['CONSUMER_SECRET']
AT=os.environ['ACCESS_TOKEN']
AS=os.environ['ACCESS_TOKEN_SECRET']

# StreamListenerを継承するクラスListener作成
class Listener(tweepy.StreamListener):
    def on_status(self, status):
        status.created_at += timedelta(hours=9)#世界標準時から日本時間に

        print('------------------------------')
        print(status.text)
        print("{name}({screen}) {created} via {src}\n".format(
                                                               name=status.author.name, screen=status.author.screen_name,
                                                               created=status.created_at, src=status.source))
        return True

    def on_error(self, status_code):
        print('エラー発生: ' + str(status_code))
        return True

    def on_timeout(self):
        print('Timeout...')
        return True

# Twitterオブジェクトの生成
auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AT, AS)

 # Listenerクラスのインスタンス
listener = Listener()

# 受信開始
stream = tweepy.Stream(auth, listener)

# キーワード引数languagesで、日本語のツイートのみに絞る
#stream.sample(languages=['ja'])

stream.filter(track = ["iput word which you want to find"])# 指定の検索ワードでフィルタ
