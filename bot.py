# -*- coding: utf-8 -*-
import rnn_easy
import json # 標準のjsonモジュールとconfig.pyの読み込み
from requests_oauthlib import OAuth1Session # OAuthのライブラリの読み込み
import time
import os

txt = rnn_easy.display(txt_file_name="mecab2019-07-12-02.txt", rnn_file_name="Rnn2019-07-12-02.pkl")

ut = time.time()

twitter = OAuth1Session(os.environ["CONSUMER_KEY"],  os.environ["CONSUMER_SECRET"], os.environ["ACCESS_TOKEN_KEY"], os.environ["ACCESS_TOKEN_SECRET"]) #認証処理

url = "https://api.twitter.com/1.1/statuses/update.json" # ツイートポストエンドポイント

# print("内容を入力してください。")
# tweet = input('>> ') #キーボード入力の取得
# print('*******************************************')
tweet = txt

params = {"status": tweet}

res = twitter.post(url, params=params)  # post送信

if res.status_code == 200:  # 正常投稿出来た場合
    print("Success.")
else:  # 正常投稿出来なかった場合
    print("Failed. : %d" % res.status_code)
