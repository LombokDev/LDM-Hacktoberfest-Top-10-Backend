import os

DEBUG = True

SQLALCHEMY_TRACK_MODIFICATIONS = False

THREADS_PER_PAGE = 2

APP_NAME = 'Lombok Dev - Top 10 Hacktoberfest'

SECRET_KEY = "cBWegL8d367vPzTp9Y2pJudLLtaKi5Jtw8//WsRjZrc="

GITHUB_ACCOUNTS = "https://docs.google.com/spreadsheets/d/e/2PACX-1vR5kNeVQR2yLePb1-Q5u7i9-cE5whC_pWleAqaGnZNqAUcaNk6BGHQ854egtsHX5HRBy3nsgoiB88cc/pub?gid=735228034&single=true&output=csv"

example = '''[
  {
    "nama": "Khairul Imam",
    "foto": "https://avatars2.githubusercontent.com/u/10706983?s=460&v=4",
    "progress": "5",
    "detail": "https://hacktoberfest.digitalocean.com/stats/khyrulimam"
  },
  {
    "nama": "Faisal Kholid",
    "foto": "https://avatars3.githubusercontent.com/u/32019765?s=200&v=4",
    "progress": "4",
    "detail": "https://hacktoberfest.digitalocean.com/stats/lombokdev"
  },
  {
    "nama": "Faisal Kholid",
    "foto": "https://avatars3.githubusercontent.com/u/32019765?s=200&v=4",
    "progress": "4",
    "detail": "https://hacktoberfest.digitalocean.com/stats/lombokdev"
  },
  {
    "nama": "Faisal Kholid",
    "foto": "https://avatars3.githubusercontent.com/u/32019765?s=200&v=4",
    "progress": "4",
    "detail": "https://hacktoberfest.digitalocean.com/stats/lombokdev"
  },
  {
    "nama": "Faisal Kholid",
    "foto": "https://avatars3.githubusercontent.com/u/32019765?s=200&v=4",
    "progress": "4",
    "detail": "https://hacktoberfest.digitalocean.com/stats/lombokdev"
  },
  {
    "nama": "Faisal Kholid",
    "foto": "https://avatars3.githubusercontent.com/u/32019765?s=200&v=4",
    "progress": "4",
    "detail": "https://hacktoberfest.digitalocean.com/stats/lombokdev"
  },
  {
    "nama": "Faisal Kholid",
    "foto": "https://avatars3.githubusercontent.com/u/32019765?s=200&v=4",
    "progress": "4",
    "detail": "https://hacktoberfest.digitalocean.com/stats/lombokdev"
  },
  {
    "nama": "Faisal Kholid",
    "foto": "https://avatars3.githubusercontent.com/u/32019765?s=200&v=4",
    "progress": "4",
    "detail": "https://hacktoberfest.digitalocean.com/stats/lombokdev"
  },
  {
    "nama": "Faisal Kholid",
    "foto": "https://avatars3.githubusercontent.com/u/32019765?s=200&v=4",
    "progress": "4",
    "detail": "https://hacktoberfest.digitalocean.com/stats/lombokdev"
  },
  {
    "nama": "Faisal Kholid",
    "foto": "https://avatars3.githubusercontent.com/u/32019765?s=200&v=4",
    "progress": "4",
    "detail": "https://hacktoberfest.digitalocean.com/stats/lombokdev"
  }
]'''