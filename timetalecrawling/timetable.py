from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
import pymysql

result=[]

connect = pymysql.connect(host='localhost', user='root', password='rootroot', db='mysql') #mysql DB와 연결
cursor = connect.cursor() #파이썬에서 쿼리 사용, 데이터 전달을 위한 cursor 인스턴스 선언

driver= webdriver.Chrome()
driver.implicitly_wait(1)

url = 'http://everytime.kr/timetable'

driver.get(url)
driver.find_element_by_name('userid').send_keys('chaew97')
driver.find_element_by_name('password').send_keys('ca6790pm')
driver.find_element_by_xpath("""//*[@id="container"]/form/p[3]/input""").click() #로그인 버튼 클릭
driver.implicitly_wait(3)
driver.find_element_by_xpath("""//*[@id="container"]/ul/li[1]""").click() #수업목록에서 검색 클릭
sleep(2)
driver.find_element_by_xpath('//*[@id="sheet"]/ul/li[3]/a').click() #자동으로 뜨는 팝업창 닫음

for l in range(5): #학교 내 전공 수 만큼 i개수 제한
    while True:
        try:
            driver.find_element_by_xpath("""//*[@id="subjects"]/div[1]/a[3]""").click() #전공/영역 클릭
            sleep(2)
            break
        except:
            continue
    while l == 0: #i가 0일경우는 전공/영역을 처음으로 들어갔을 때만 <전공, 교양, 교직, 사이버> 중에 골라야 함
        try:
            driver.find_element_by_xpath("""//*[@id="subjectCategoryFilter"]/div/ul/li[1]""").click() #전공 메뉴 클릭
            sleep(2)
            break
        except:
            continue
    while True:
        try:
            driver.find_element_by_xpath("""//*[@id="subjectCategoryFilter"]/div/ul/ul[1]/li["""+str((l+1))+"""]""").click() #전공 차례대로 클릭
            sleep(2)
            break
        except:
            continue


    page = driver.page_source  # 웹페이지 긁어옴
    soup = BeautifulSoup(page, "html.parser")  # 페이지를 soup객체로 만듦
    results = []
    #list = soup.find('div', {'class': 'list'}).find('tbody').find_all('td')
    trs = soup.select('#subjects > div.list > table > tbody > tr')
    for i in trs:
        result = []
        tds = i.select('#subjects > div.list > table > tbody > tr > td')
        result.append(tds[1].text)  # 캠퍼스
        result.append(tds[2].text)  # 과목코드
        result.append(tds[3].text)  # 과목명
        result.append(tds[4].text)  # 교수
        result.append(tds[5].text)  # 학점
        result.append(tds[6].text)  # 강의시간(강의실) ex)월-4,5,6(성607)
        result.append(tds[7].text)  # 학년구분
        results.append(result)
    print(results)

    for d in results:
        code = str(d[1])
        campus = str(d[0])
        subject = str(d[2])
        professor = str(d[3])
        credits = str(d[4])
        time_location = str(d[5])
        grade = str(d[6])

        sql = """INSERT INTO test_subject(code, campus, subject, professor, credits, time_location, grade) VALUES('%s', 
        '%s', '%s', '%s', '%s', '%s', '%s') """ % (code, campus, subject, professor, credits, time_location, grade)

        cursor.execute(sql)
        connect.commit()

connect.close()


    #break

### 수정해야될 사항 ###
# 반복문 l 범위 수동입력이 아닌 자동 입력될 수 있게 수정
# 위 사항을 제외한 전공 부분은 완성했지만 교양 부분도 xpath 계산해서 받아와야함
# DB INSERT 구문에서 값이 있을 경우 UPDATE 될 수 있도록 수정





