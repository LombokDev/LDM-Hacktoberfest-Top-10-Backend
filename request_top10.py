import requests
from bs4 import BeautifulSoup





def get_data(driver, username):
  try:
    url = "https://hacktoberfest.digitalocean.com/stats/%s" % username
    req = requests.get(url)
    assert req.ok
    driver.get(url)
    html_string = driver.page_source
    parser = BeautifulSoup(html_string, 'lxml')
    image = parser.find('img', {'class': 'userstats--card-image'})
    name = parser.find('h2')
    progress = parser.find('span', {'data-js': 'userPRCount'})
    return {
      "nama": name.text,
      "foto": image.get('src'),
      "progress": progress.text,
      "detail": url
    }
  except Exception:
    return {
    "nama": "%s - Akun belum dibuat" % username,
    "foto": "https://bestbath.com/wp-content/uploads/2016/01/image-coming-soon.png",
    "progress": "0",
    "detail": "https://hacktoberfest.digitalocean.com/stats/%s" % username
  }


def post_data(data):
  req = requests.post('https://ldm5hacktoberfest.herokuapp.com/broadcast-top10', data=data)
  print(req.json())