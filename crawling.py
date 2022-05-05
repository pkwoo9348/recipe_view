from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# selenium에서 사용할 웹 드라이버 절대 경로 정보
chromedriver = r'C:\Users\kp\Desktop\recipe_view\chromedriver_win32\chromedriver.exe'
# selenum의 webdriver에 앞서 설치한 chromedirver를 연동한다.
driver = webdriver.Chrome(chromedriver)
# driver로 특정 페이지를 크롤링한다.
driver.get('https://www.youtube.com/c/paikscuisine/videos')
driver.implicitly_wait(5)

#스크롤 마지막까지 내리기
before_h = driver.execute_script("return window.scrollY")
while True:
    driver.find_element_by_css_selector('body').send_keys(Keys.END)
    time.sleep(2)
    
    after_h=driver.execute_script("return window.scrollY")
    
    if after_h==before_h:
        break
    
    before_h = after_h


#url 가져오기
url_lists=driver.find_elements_by_css_selector("a.yt-simple-endpoint.style-scope.ytd-grid-video-renderer")

for url_list in url_lists:
    url=url_list.get_attribute("href")
    print(url)