# coding: utf-8

from slackclient import SlackClient
import time
import subprocess
import re

slack_token = sys.argv[0]

sc = SlackClient(slack_token)

if sc.rtm_connect():
  while sc.server.connected is True:
    response = sc.rtm_read()
    for data in response:
      if 'type' in data and 'text' in data:
        if data['type'] == 'message':
          message = data['text'].strip()
          message = re.sub(r'[!-/]', "", message)
          message = re.sub(r'[\[-\`]', "", message)
          message = re.sub(r'[\{-\~]', "", message)
          message = re.sub('\n', " ", message)
          message = re.sub(';', "", message)
          cmd = '/usr/bin/say ' + '"' + message + '"'
          subprocess.run(cmd, shell=True)
          print(message)

    time.sleep(3)
else:
  print("Connection Failed")
