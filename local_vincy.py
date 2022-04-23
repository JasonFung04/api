# encoding:utf-8

'''
environment: D:\software\Anaconda\envs\ComplexEquipKGQA
'''

import os
import itchat
import json
from sanic import Sanic, response
from sanic_cors import CORS
from sanic_openapi import swagger_blueprint, doc

#from modules import chitchat_bot, classifier
# medical_bot
# from utils.json_utils import dump_user_dialogue, load_user_dialogue_context

def delete_cache(file_name):
    """
    清除缓存数据，切换账号登入
    :param file_name:
    :return:
    """
    if os.path.exists(file_name):
        os.remove(file_name)

@itchat.msg_register(["Text"]) #msg_type
def text_reply(msg):
    """
    微信入口
    :param msg:
    :return:
    """
   # user_intent= classifier(msg["Text"])  #对用户输入进行初分类
   # print("user_intent:", user_intent)
   # if user_intent in ["greet","goodbye","deny","isbot"]:
   #     reply=chitchat_bot(user_intent)


   #     msg.user.send(reply)


""""
部署网页接口
"""
app=Sanic(__name__)
CORS(app)

app.blueprint(swagger_blueprint)
app.config["API_VERSION"]="0.1"
app.config["API_ITILE"]="DIALOG_SERVICE: Sanic-OpenAPI"

server_port=int(os.getenv('SERVER_PORT', 12348))
@app.post("/bot/message")
@doc.summary("Let us have a chat")
@doc.consumes(doc.JsonBody({"message": str}), location="body")
def message(request):
    """
    sanic入口
    :param request:
    :return:
    """
    # 获取用户ID和用户输入
   # sender=request.json.get("sender")
   # message=request.json.get("message")
   # print("sender:{},message:{}".format(sender,message))
    # 对话开始新建小本本

    # 判断用户意图是否属于闲聊类
 #   user_intent = classifier(message)
 #   print("user_intent:", user_intent)
 #   if user_intent in ["greet", "goodbye", "deny", "isbot"]:
  #      reply = chitchat_bot(user_intent)
    



 #   return response.json(reply)


if __name__=='__main__':
    """
    测试用例：
    你好
    你是机器人吗
    再见
    不是这样的
    """
    # 打开下面注释可以清楚对话日志缓存
    # delete_cache(file_name='/logs/loginInfo.pkl')

    # 打开下面日志使用微信进行对话
    # itchat.auto_login(hotReload=True, enableCmdQR=2, statusStorageDir='./logs/loginInfo.pkl')
    # itchat.run()
  

    # 打开下面对话使用swagger在网页段进行对话
    app.run()  #ps 链接已经建立 但网址在浏览器打不开


