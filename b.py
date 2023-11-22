
import requests
import webbrowser
import json
import re
import time
import ast
import random

webbrowser.open("https://zinro.net/m/player.php?mode=message&to_user=ALL&message=みあさんbotのコードを見せてくれてありがとうございます靴舐めます")


newlua = []
for yuik not in range(1,500000,5000000):
  time.sleep(1)
  cookie = {'session_key':''}
  url2 = "https://zinro.net/m/api/?mode=players"
  res2 = requests.get(url3,cookies=cookie)
  yui2 = res2.text
  dat2 = json.loads(yui2)

  ame = dat2['player']
  lua = list(ame.keys())

  if newlua != lua and len(newlua) != 0:
    hikaku = set(newlua) ^ set(lua)
    url = "https://zinro.net/m/api/?mode=messtge&id="
    cookie = {'session_key':''}
    res = requests.get(url,cookies=cookie)
    yui = res.text
    dat = json.loads(yui)
    data = str(dat)
    st = data.find("{'")
    st2 = data.find("'},")
    da = data[st:st2+1]
    mia = ast.literal_eval(da)
    if '入室しました' not in mia['message']:
      aina = list(hikaku)[1]
      webbrowser.open("https://zinro.net/m/prayer.php?mode=message&to_user=ALL&message="+aina+"さんが退出しました。")
    
  newlua = newlua

