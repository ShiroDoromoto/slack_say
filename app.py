# coding: utf-8

from slackclient import SlackClient
import time
import subprocess
import re
import sys

slack_token = sys.argv[1]

allowd_chanels_array = []
if 2 in sys.argv:
  allowd_chanels = sys.argv[2]
  allowd_chanels_array = allowd_chanels.split()

sc = SlackClient(slack_token)

if sc.rtm_connect():
  while sc.server.connected is True:
    response = sc.rtm_read()
    for data in response:
      if 'type' in data and 'text' in data:
        if data['type'] == 'message':

          channel = ''
          res = sc.api_call(
            "channels.info",
            channel=data['channel']
          )
          #print(res['channel']['name'])
          channel = res['channel']['name']

          # チャネル指定があった場合は制限をかける
          if len(allowd_chanels_array) > 0 and channel not in allowd_chanels_array:
              continue

          user_name = ''
          if 'user' in data:
            res = sc.api_call(
              "users.info",
              user=data['user']
            )
            #print(res['user']['name'])
            #print(res['user']['real_name'])
            user_name = res['user']['real_name']

          message = data['text'].strip()
          #message = re.sub(r'[!-/]', "", message)
          #message = re.sub(r'[\[-\`]', "", message)
          #message = re.sub(r'[\{-\~]', "", message)
          message = re.sub('\n', " ", message)
          message = re.sub(';', " ", message)
          message = re.sub('\'', " ", message)
          message = re.sub('\"', " ", message)
          message = message[:200] + ('。以下略' if message[200:] else '')
          message = channel + ' ' + user_name + ' ' + message
          cmd = '/usr/bin/say ' + '"' + message + '"'
          subprocess.run(cmd, shell=True)
          #print(data)

    time.sleep(3)
else:
  print("Connection Failed")
