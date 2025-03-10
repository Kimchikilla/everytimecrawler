from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

# 환경 변수에서 로그인 정보 가져오기
USER_ID = os.getenv("EVERYTIME_USER_ID")
USER_PW = os.getenv("EVERYTIME_USER_PW")

# 크롬 드라이버 설정 (드라이버 경로를 지정해줘야 함)
chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome("C:/Users/USER/Downloads/chromedriver_win32/chromedriver.exe", options=chrome_options)

# 에브리타임 로그인 페이지 접속
driver.get("https://everytime.kr/login")

# 아이디 입력
id_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "userid"))
)
id_input.send_keys(USER_ID)

# 비밀번호 입력
pw_input = driver.find_element(By.NAME, "password")
pw_input.send_keys(USER_PW)
pw_input.send_keys(Keys.RETURN)  # 엔터 키 입력

# 강의평 페이지 이동
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "lecture"))
)
driver.get("https://everytime.kr/lecture")

# 강의 리스트 가져오기
lectures = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "lecture"))
)

for lecture in lectures:
    subject = lecture.find_element(By.CLASS_NAME, "subject").text
    professor = lecture.find_element(By.CLASS_NAME, "professor").text
    rating = lecture.find_element(By.CLASS_NAME, "rating").text
    review = lecture.find_element(By.CLASS_NAME, "review").text
    
    print(f"과목: {subject}, 교수: {professor}, 평점: {rating}, 후기: {review}")

# 크롤링 완료 후 브라우저 종료
driver.quit()
