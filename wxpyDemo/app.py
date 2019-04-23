from wxpy import *
import time

#初始化机器人，扫码登录
bot = Bot()

#搜索好友
# frend_one = bot.friends().search('张竞予')[0]

# print(bot)
# print(bot.friends())
# print(type(frend_one))

#发消息
# frend_one.send('给我发消息')

# while True:
#     time.sleep(3)
#     frend_one.send('Hello 小伙计')

#响应消息
# @bot.register()
# def reply_friend(msg):
#     return '主人不在，请一万年后联系！（此消息为自动回复）'
    # return 'received: {} ({})'.format(msg.text, msg.type)

# 报错
# bot.self.add()
# bot.self.accept()
# bot.self.send('开始消息接收')

#  群消息响应
@bot.register()
def reply_friend(msg):
    bot.file_helper.send(msg.text)

# 机器人账号自身
# myself = bot.self

# 向文件传输助手发送消息
# bot.file_helper.send('Hello from wxpy!')

# 进入 Python 命令行、让程序保持运行
embed()

# 或者仅仅堵塞线程
# bot.join()