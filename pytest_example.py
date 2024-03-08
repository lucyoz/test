from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import pytest

@pytest.fixture(scope="function")
def setup():
    options = Options()
    options.add_argument("--headless")      # GUI 없이 실행
    options.add_argument("--no-sandbox")    # Sandbox 모드 비활성화
    options.add_argument("--disable-dev-shm-usage") # /dev/shm 파티션 사용 안함
    options.add_argument("--disable-gpu")   # GPU 가속 비활성화, headless 모드에서 권장

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=options)
            
    #driver.get("https://www.google.com/")
    
    #request.cls.driver = driver
    yield driver
    driver.quit()
    
@pytest.mark.description("google 홈에서 상단 gmail 메뉴 클릭")
def test_link_to_gmail(setup):
    setup.get("https://www.google.com/")
    gmail_link = setup.find_element(By.XPATH, '//a[text()="Gmail"]')
    gmail_link.click()
    setup.implicitly_wait(10)
        
    try: 
        excepted_url = "account"
        actual_url = setup.current_url
            
        assert excepted_url in actual_url
        print("Gmail page loaded successfully")
    except AssertionError as e:
        print(f"AssertionError: Gmail page failed to load: {e}: {actual_url}")
    except NoSuchElementException as ex:
        print(f"NoSuchElementException: Gmail page failed to load: {ex}")
    except Exception as exc:
        print(f"Exception: Gmail page failed to load: {exc}")
            
@pytest.mark.description("google 홈에서 상단 이미지 메뉴 클릭")      
def test_doodles(setup):
    setup.get("https://www.google.com/")
    images_link = setup.find_element(By.XPATH, '//a[text()="이미지"]')
    images_link.click()
    setup.implicitly_wait(10)
        
    try: 
        excepted_url = "https://www.google.com/imghp?hl=ko&ogbl"
        actual_url = setup.current_url
            
        assert excepted_url in actual_url
        print("Gmail page loaded successfully")
    except AssertionError as e:
        print(f"AssertionError: Gmail page failed to load: {e}: {actual_url}")
    except NoSuchElementException as ex:
        print(f"NoSuchElementException: Gmail page failed to load: {ex}")
    except Exception as exc:
            print(f"Exception: Gmail page failed to load: {exc}")
 