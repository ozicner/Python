from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd
import numpy as np
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('headless')
# chrome_options.add_argument('window-size=1920x1080')
# chrome_options.add_argument('disable-gpu')
# chrome_options.add_argument('lang=ko_KR')
driver = webdriver.Chrome('chromedriver.exe', options=chrome_options)
# 다음 주소로 이동
url = 'https://map.naver.com/v5/search/강남역%20맛집?c=14140182.6030886,4508742.0199864,15,0,0,0,dh'
driver.get(url)
delay = 3
driver.implicitly_wait(delay)
# driver.get_screenshot_as_file('s0.png')
# print(driver.page_source)   # html 소스 보기
# 데이터 리스트로 저장
name = []
category = []
rating = []
review_count = []
blog_count = []
location = []
# #document 경로를 찾고 switch_to.frame 으로 상호 목록 html 을 전환함
scroll_frame = driver.find_element_by_id('searchIframe')
driver.switch_to.frame(scroll_frame)
driver.implicitly_wait(delay)
# while True:
#     button_element = driver.find_elements_by_class_name('_3pA6R')[1]
#     print(button_element.value_of_css_property('opacity'))
# #     if button_element.is_enabled() == False:
# #         driver.quit()
# #         break
#     button_element.click()
# print('hahahah')
# a = driver.find_elements_by_class_name('_3pA6R')[1]
for _ in range(1):
    delay_int = np.random.randint(1, 5)
    delay = np.random.rand() + delay_int
    # scroll container 의 xpath 를 찾음
    scroll_container = driver.find_element_by_id('_pcmap_list_scroll_container')
    driver.implicitly_wait(delay)
    # 맛집 목록의 스크롤을 내림
    for _ in range(7):
        driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scroll_container)
        time.sleep(1)
        # test 하기 위해 스크롤을 전부 내린 후 스샷으로 저장
        # driver.get_screenshot_as_file('s3.png')
        # [@class="Tx7az" "_36o75 _3jJcF"]
        # 식당 클릭
    # scroll container 안의 모든 식당들을 클릭하기
    elements = driver.find_elements_by_xpath('//*[@class="Tx7az"]')
    for element in elements:
        delay_int = np.random.randint(1, 5)
        delay = np.random.rand() + delay_int
        element.click()  # element, 상호명으로 된 버튼을 클릭함
        # 클릭하면 새로운 html 이 생성됨, 그것에 접속하고 그 html 을 beautiful soup 에 넣어 html 을 크롤링해야함
        time.sleep(delay)
        driver.switch_to.default_content()  # 상위 프레임으로 전환 (root frame)
        # 가게 정보 html 로 전환
        info_frame = driver.find_element_by_id('entryIframe')
        driver.switch_to.frame(info_frame)
        driver.implicitly_wait(delay)
        # 소스 가져오기
        req = driver.page_source
        soup = BeautifulSoup(req, 'html.parser')
        title = soup.select('#_title')
        # 이름, 카테고리
        for child in title:
            name.append(child.contents[0].string)
            category.append(child.contents[1].string)
        # 주소
        location.append(soup.select('._2yqUQ')[0].string)
        # 별점, 방문자리뷰, 블로그리뷰
        points = title[0].find_next_siblings()[0].find_all('span')
        # 3개에서 하나라도 없으면 패스
        if len(points) != 3:
            driver.switch_to.default_content()
            driver.switch_to.frame(scroll_frame)
            continue
        # 평점, 방문자 리뷰 개수, 블로그 리뷰 추가
        rating.append(float(list(points[0].strings)[0]))
        review_count.append(int(list(points[1].strings)[2].replace(',', '')))
        blog_count.append(int(list(points[2].strings)[2]))
        #     for point in points:
        #         if '/5' in point.strings:
        #             rating.append(float(list(point.strings)[0]))
        #         elif '방문자리뷰' in point.strings:
        #             review_count.append(int(list(point.strings)[2].replace(',', '')))
        #         elif '블로그리뷰' in point.strings:
        #             blog_count.append(int(list(point.strings)[2]))
        # 상위 프레임으로 전환 (root frame)
        driver.switch_to.default_content()
        driver.switch_to.frame(scroll_frame)
        # test 하기 위해 상호를 클릭할 때마다 스샷을 찍어 저장함
        # driver.get_screenshot_as_file(str(idx) + '.png')
    # ******** 여기서 부터 html
    a = driver.find_elements_by_class_name('_3pA6R')[1]
    driver.find_elements_by_class_name('_3pA6R')[1].click()
driver.quit()
# time.sleep(delay)
#
# driver.get_screenshot_as_file('s3.png')