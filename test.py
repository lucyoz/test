from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

# Chrome WebDriver 인스턴스 생성 - 
driver = webdriver.Chrome(ChromeDriverManager().install())

# Google 홈페이지 열기
# driver.get("https://www.google.com/")

# Gmail 링크 클릭을 위한 요소 찾기
# gmail_link = driver.find_element(By.XPATH, '//a[text()="Gmail"]')

# Gmail 링크 클릭
# gmail_link.click()

# 몇 초 동안 페이지 로드를 기다린 후에 종료 (실제 사용시에는 페이지 로드 완료까지 기다리는 로직을 추가하는 것이 좋습니다)
# driver.implicitly_wait(10) # 10초 대기
# driver.close()