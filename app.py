# coding: utf-8

from slackclient import SlackClient
import time
import subprocess
import re
import sys

slack_token = sys.argv[1]

sc = SlackClient(slack_token)

if sc.rtm_connect():
  while sc.server.connected is True:
    response = sc.rtm_read()
    for data in response:
      if 'type' in data and 'text' in data:
        if data['type'] == 'message':

          res = sc.api_call(
            "channels.info",
            channel=data['channel']
          )
          #print(res['channel']['name'])
          channel = res['channel']['name']

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
          message = message[:100] + ('。以下略' if message[100:] else '')
          message = channel + ' ' + user_name + ' ' + message
          cmd = '/usr/bin/say ' + '"' + message + '"'
          subprocess.run(cmd, shell=True)
          #print(data)

    time.sleep(3)
else:
  print("Connection Failed")
