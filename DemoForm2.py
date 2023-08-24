# DemoForm2.py 
# DemoForm2.ui(화면을 저장) + DemoForm2.py(로직을 저장)
import sys 
from PyQt5.QtWidgets import * 
from PyQt5 import uic 
#웹서버에 통신
import requests
#크롤링
from bs4 import BeautifulSoup


#디자인 파일을 로딩(파일명 수정) 
form_class = uic.loadUiType("DemoForm2.ui")[0]

#폼 클래스 정의(QMainWindow상속)
class DemoForm(QMainWindow, form_class):
    #초기화 메서드
    def __init__(self):
        super().__init__() 
        self.setupUi(self)
    def firstClick(self):
        url = "https://www.daangn.com"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        posts = soup.find_all("div", attrs={"class":"card-desc"})
        f = open("c:\\work\\daangn.txt", "a+", encoding="utf-8")
        for post in posts:
            titleElem = post.find("h2", attrs={"class":"card-title"})
            priceElem = post.find("div", attrs={"class":"card-price"})
            addrElem = post.find("div", attrs={"class":"card-region-name"})
            title = titleElem.text.replace("\n", "") 
            price = priceElem.text.replace("\n", "")
            addr = addrElem.text.replace("\n", "")
            print(f"{title}, {price}, {addr}")
            f.write(f"{title}, {price}, {addr}\n")
        f.close() 
        self.label.setText("당근 마켓 크롤링 완료")        
    def secondClick(self):
        self.label.setText("두번째 버튼 클릭")        
    def thirdClick(self):
        self.label.setText("세번째 버튼 클릭했음~~")        


#직접 모듈을 실행했는지 체크 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoForm = DemoForm() 
    demoForm.show()
    app.exec_()


