from selenium import webdriver
import time
from bs4 import BeautifulSoup

import tweepy
import time

api_key = 'secret'
api_key_secret = 'secret'
access_token = 'secret'
access_token_secret = 'secret'

authenticator = tweepy.OAuthHandler(api_key, api_key_secret)
authenticator.set_access_token(access_token, access_token_secret)

api = tweepy.API(authenticator, wait_on_rate_limit=True)

driver = webdriver.Edge()
url= "https://atletico.com.br/home"
driver.maximize_window()
driver.get(url)

time.sleep(5)
content = driver.page_source.encode('utf-8').strip()
soup = BeautifulSoup(content,"html.parser")

game = soup.find("h2",{"nextGame-section-body-hashtag"})
competition = soup.find("h2",{"nextGame-section-body-text nextGame-text-gray-200 fs-16 fw-400 text-gray-200"})
when = soup.find("h2",{"nextGame-section-body-text fs-20 text-white fw-400"})

game_text = game.get_text()
competition_text = competition.get_text()
when_text = when.get_text()

galo = ("Próximo jogo 🐓:  " + game_text + "\n" + 
        "Competição: " + competition_text + "\n" + 
        "Quando e onde acontecerá: " + when_text)
print(galo)

api.update_status(galo)

message = ("@{}, o próximo jogo do galo é " + game_text + ", que é uma disputa pela competição " + competition_text + " e que acontecerá em " + when_text)

mentions = api.mentions_timeline()
for mention in mentions:
        api.update_status(message.format(mention.author.screen_name))
                
driver.quit() 
        


