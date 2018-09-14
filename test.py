#coding: utf-8

from __future__ import absolute_import, division, print_function
from bottle import route, run, request,static_file
 
import simplejson as json
import logging

from flask import Flask, request, jsonify


app = Flask(__name__)


class Message(object):
    """Slackのメッセージクラス"""
    token = "WHDw3qxvx4b6LdC7aHaSz3GQ"
    team_id = "T0001"
    channel_id = "C2147483705"  # 投稿されたチャンネルID
    channel_name = "forest"  # チャンネル名
    timestamp = 0
    user_id = "U2147483697"  
    user_name = "username"  # 投稿ユーザー名
    text = "test"  # 投稿内容
    trigger_word = "pi:"  # OutgoingWebhooksに設定したトリガー
    

    def __init__(self, params):
        self.team_id = params["team_id"]
        self.channel_id = params["channel_id"]
        self.channel_name = params["channel_name"]
        self.timestamp = params["timestamp"]
        self.user_id = params["user_id"]
        self.user_name = params["user_name"]
        self.text = params["text"]
        self.trigger_word = params["trigger_word"]
        print(params)

    def __str__(self):
        res = self.__class__.__name__
        res += "@{0.token}[channel={0.channel_name}, user={0.user_name}, text={0.text}]".format(self)
        return res


@app.route('/', methods=['POST'])
def mybot():
    print("Hello world")
    msg = Message(request.form)
    logging.debug(msg)
    print(msg)

    # slackbotによる投稿は無視(無限ループ回避)
    if msg.user_name == "slackbot":
        return ''
    # 投稿にyoが含まれてたらyoを返す  
    if "yo" in msg.text:
        return _say("yo")
    return ''


def _say(text):
    """Slackの形式でJSONを返す"""
    return jsonify({
        "text": text, # 投稿する内容
        "username": "mybot", # bot名
        "icon_emoji": "", # botのiconを絵文字の中から指定
    })

if __name__ == '__main__':
    run(host='192.168.100.134', port=8889, debug=True, reloader=True)


