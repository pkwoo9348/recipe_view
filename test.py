# test용 파일
# test 후 병합
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By



# selenium에서 사용할 웹 드라이버 절대 경로 정보
chromedriver = r'C:\Users\kp\Desktop\recipe_view\chromedriver_win32\chromedriver.exe'
# selenum의 webdriver에 앞서 설치한 chromedirver를 연동한다.
driver = webdriver.Chrome(chromedriver)
# driver로 특정 페이지를 크롤링한다.

url = 'https://www.youtube.com/watch?v=e--h7ax_6pQ'

driver.get(url)
driver.implicitly_wait(5)


coments=driver.find_elements(By.CSS_SELECTOR, 'span.style-scope.yt-formatted-string')


for coment in coments:
    print(coment.text)
