from selenium import webdriver #Selenium Webdriverをインポートして
from selenium.webdriver.common.keys import Keys
import urllib.parse
import time
import random
import settings

browser = webdriver.Chrome("/usr/local/bin/chromedriver") #Chromeを動かすドライバを読み込み

loginURL = "https://www.instagram.com/" #ログインする際のページ
tagSearchURL = "https://www.instagram.com/explore/tags/{}/?hl=ja" #.format()で{}の中の値を入れられるようになっている

tagName = "ワンピースコーデ" #タグの名前 #よみうりランド


#selectors
#ここには書くページのSelectorを選ぶ。x-pathもしくはcss selector

loginPath = '//*[@id="react-root"]/section/main/article/div[2]/div[2]/p/a' #xpath @https://www.instagram.com/

notNowPath = '//*[@id="react-root"]/div/div[2]/a[2]'

mediaSelector = 'div.v1Nh3' #表示されているメディアのwebelement @https://www.instagram.com/explore/tags/%E3%82%88%E3%81%BF%E3%81%86%E3%82%8A%E3%83%A9%E3%83%B3%E3%83%89/?hl=ja
nextPagerSelector = 'a.coreSpriteRightPaginationArrow' #次へボタン

#USER INFO

username = settings.username
password = settings.password 

#list

mediaList = []

#counter

likedCounter = 0

if __name__ == '__main__':

    #Login 
    browser.get(loginURL)
    time.sleep(2)
    # browser.find_element_by_xpath(loginPath).click()
    # time.sleep(3)
    usernameField = browser.find_element_by_name("username")
    usernameField.send_keys(username)
    passwordField = browser.find_element_by_name("password")
    passwordField.send_keys(password)
    passwordField.send_keys(Keys.RETURN)

    #Finished logging in. now at 
    time.sleep(3)
    encodedTag = urllib.parse.quote(tagName) #普通にURLに日本語は入れられないので、エンコードする
    encodedURL = tagSearchURL.format(encodedTag)
    print("encodedURL:{}".format(encodedURL))
    browser.get(encodedURL)

    #Finished tag search. now at https://www.instagram.com/explore/tags/%E8%AA%AD%E5%A3%B2%E3%83%A9%E3%83%B3%E3%83%89/?hl=ja
    time.sleep(3)
    browser.implicitly_wait(10)

    #写真を取得してクリックする

    mediaList = browser.find_elements_by_css_selector(mediaSelector)
    mediaCounter = len(mediaList)
    print("Found {} media".format(mediaCounter))

    for media in mediaList:
        media.click()

        # 次へボタンが表示されるまで
        while True:
            try:
                # abc = random.randint(random.randint(20, 100), random.randint(110, 180))
                # print(str(abc)+"秒待機します")
                time.sleep(6)
                browser.find_element_by_class_name("fr66n").click()
                browser.implicitly_wait(10)
                likedCounter += 1
                print("liked {} of {}".format(likedCounter,mediaCounter))
                browser.find_element_by_css_selector(nextPagerSelector).click()
            except Exception as e:
                print(e)
                browser.find_element_by_css_selector(nextPagerSelector).click()
        break #for文自体も終了させる

    print("You liked {} media".format(likedCounter))