from selenium import webdriver
import time
import requests

class Libook:
    def __init__(self):
        self.start_url = "https://lfs.bookln.cn/book/sample1.htm?id=57587&shelfId=4995"
        self.driver = webdriver.Chrome(executable_path="chromedriver.exe")
        self.i = 2

    def get_content(self):
        time.sleep(3)
        img = self.driver.find_element_by_xpath("//div[@class='page p"+str(self.i)+" even']//img").get_attribute("src")
        img1 = self.driver.find_element_by_xpath("//div[@class='page p"+str(self.i+1)+" odd']//img").get_attribute("src")

        return img, img1

    def save_img(self, img_src):
        re = requests.get(img_src)
        with open("./img/"+str(self.i)+".png", "wb") as f:
            f.write(re.content)
    def run(self):
        # 发送请求
        self.driver.get(self.start_url)
        time.sleep(3)
        self.driver.find_element_by_xpath("//span[@class='iconfont nexPage']").click()
        while self.i<60:
            # 获取图片url
            img_src, img_src1= self.get_content()
            print(img_src)
            print(img_src1)
            # 保存图片
            self.save_img(img_src)
            self.i = self.i + 1
            self.save_img(img_src1)
            self.i = self.i + 1
            # 点击下一页url
            self.driver.find_element_by_xpath("//span[@class='iconfont nexPage']").click()

        self.driver.quit()
if __name__ == '__main__':
    i = Libook()
    i.run()