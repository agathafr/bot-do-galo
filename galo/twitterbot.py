from selenium import webdriver
import time
from bs4 import BeautifulSoup

import tweepy
import time

api_key = 'BgT04hElJfXhh0JJcHp49ELpI'
api_key_secret = 'AnpvB7iZ9svp5fstLzFNOBoegCbdc27iWhZkSyR3RfP2nWlyBl'
access_token = '1452432763890683913-FAjfqOnnfEJaoeZjQlB1SWdYCffOWy'
access_token_secret = '8IEOBj52DxBNFdx8tr5jbt4vcOWBBQ8cbL4qBlJfRzGIi'

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

# container = soup.find("div", {"col-12 col-md-6 pr-md-0"})
# print(container.text)

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

#words = ["quando", "proximo", "próximo"]
#if [word in mention.text for word in words]:

message = ("@{}, o próximo jogo do galo é " + game_text + ", que é uma disputa pela competição " + competition_text + " e que acontecerá em " + when_text)

mentions = api.mentions_timeline()
for mention in mentions:
        api.update_status(message.format(mention.author.screen_name))
                
#search = 'O galo ganhou!'

#for tweet in tweepy.Cursor(api.search_tweets, search).items(10):
#        print("nome do usuário: @" + tweet.user.screen_name)
#        api.update_status(status="@" + tweet.user.screen_name + " O galo é doido!")
#        time.sleep(30)

driver.quit() 
        


