from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

# Chrome WebDriver 인스턴스 생성 - 
#driver = webdriver.Chrome(ChromeDriverManager().install())
options = Options()
options.add_argument("--headless")      # GUI 없이 실행
options.add_argument("--no-sandbox")    # Sandbox 모드 비활성화
options.add_argument("--disable-dev-shm-usage") # /dev/shm 파티션 사용 안함
options.add_argument("--disable-gpu")   # GPU 가속 비활성화, headless 모드에서 권장
options.add_argument('--log-level=1')

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()), options=options)

# Google 홈페이지 열기
driver.get("https://www.google.com/")

# Gmail 링크 클릭을 위한 요소 찾기
gmail_link = driver.find_element(By.XPATH, '//a[text()="Gmail"]')

# Gmail 링크 클릭
gmail_link.click()

# 몇 초 동안 페이지 로드를 기다린 후에 종료 (실제 사용시에는 페이지 로드 완료까지 기다리는 로직을 추가하는 것이 좋습니다)
driver.implicitly_wait(10) # 10초 대기

try: 
    excepted_url = "account"
    actual_url = driver.current_url
    
    assert excepted_url in actual_url
    print("Gmail page loaded successfully")
except AssertionError as e:
    print(f"AssertionError: Gmail page failed to load: {e}: {actual_url}")
except NoSuchElementException as ex:
    print(f"NoSuchElementException: Gmail page failed to load: {ex}")
except Exception as exc:
    print(f"Exception: Gmail page failed to load: {exc}")

driver.close()