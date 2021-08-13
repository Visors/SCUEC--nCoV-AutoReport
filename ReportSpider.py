from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


class ReportSpider:
    # 类变量ChromeOption
    op = Options()
    op.add_argument('--headless')
    op.add_argument('--disable-gpu')
    op.add_argument('--no-sandbox')
    op.add_argument('log-level=3')

    load_fail = "Can't load this page!"  # 加载错误报头

    def __init__(self):
        # 基本信息
        self.username = 'your student_id'  # 学号
        self.password = 'your password'  # 密码
        # webdriver
        # driver用于请求界面
        self.driver = webdriver.Chrome(executable_path='./chromedriver', chrome_options=ReportSpider.op)
        self.driver.set_page_load_timeout(20)

    def run(self):
        self.driver.maximize_window()
        try:
            self.driver.get('https://ehall.scuec.edu.cn/new/index.html?browser=no')
        except:
            self.driver.close()
            raise ConnectionError(self.load_fail)

        # 登录
        self.driver.find_element_by_id('ampHasNoLogin').click()
        time.sleep(5)
        try:
            self.driver.find_element_by_id('username').send_keys(self.username)
        except:
            self.driver.close()
            raise ConnectionError(self.load_fail)
        self.driver.find_element_by_id('password').send_keys(self.password)
        self.driver.find_element_by_id('login_submit').click()
        time.sleep(5)

        # 请求填报页面
        try:
            self.driver.get('https://ehall.scuec.edu.cn/yqfw/sys/xsyqxxsjapp/*default/index.do#/mrbpa')
        except:
            self.driver.close()
            raise ConnectionError(self.load_fail)
        print('Login successfully!')
        time.sleep(7)

        # 提交
        try:
            self.driver.find_element_by_id('save').click()
        except:
            self.driver.close()
            raise ConnectionError(self.load_fail)
        self.driver.close()
        print('Report Successfully!')


if __name__ == '__main__':
    report_spider = ReportSpider()
    report_spider.run()
