import config
import requests
from request_top10 import get_data, post_data
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import os
import boot
from boot import socketio


def run():

  options = Options()
  options.headless = True
  driver = webdriver.Firefox(options=options, executable_path='%s/geckodriver' % os.getcwd())

  req = requests.get(config.GITHUB_ACCOUNTS)
  accounts = req.content
  acc_split = accounts.splitlines()
  acc_normal = list(filter(lambda item: not item.endswith(b'/'), acc_split))
  acc_not_normal = list(filter(lambda item: item.endswith(b'/'), acc_split))
  acc_normalized = [item[:-1] for item in acc_not_normal]
  map_normal = [b''.join(item.split(b'/')[-1].split(b' ')).decode() for item in acc_normal]
  map_normalized = [b''.join(item.split(b'/')[-1].split(b' ')).decode() for item in acc_normalized]
  map_normal.extend(map_normalized)

  datas = [get_data(driver, user) for user in map_normal]
  socketio.emit('top-ten', datas)

  driver.quit()