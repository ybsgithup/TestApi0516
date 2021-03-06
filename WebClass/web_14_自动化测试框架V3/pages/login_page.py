"""
PO模式， Page Object Model, 页面对象模型。
解释：
Page: 页面
Object: 对象
网页页面转化成了 python 的一个对象。
网页当中的流程操作，元素操作 ==》 对象当中的方法。
网页当中的名词，元素定位方式， ==》 python 对象的属性。

DOM

PO 带来的意义：
# 封装的方式：
# 1， 测试用例方法更加简洁
# 2， 登录方法可以重复使用
# 3， 测试用例方法当中，有没有具体的页面逻辑？？实现了页面操作和测试的分离
# 4， 当页面操作需要变化的时候，比如前段工程师修改了页面，提高了可维护性。
# 5， 面试的时候经常会问的问题。
# 6， 提高代码的可读性。
# PO， 类的方式进行封装。
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from common.base_page import BasePage
from config import config

# 一般一个Html页面，写成一个类
class LoginPage(BasePage):
    # 拼接url，baseurl已经写在config.HOST中
    url = config.HOST + "/Index/login.html"

    # 存放所有的 locator
    # 用户名定位
    mobile_locator = (By.NAME, "phone")
    # 密码元素定位
    pwd_locator = (By.NAME, "password")
    # 登录按钮定位
    login_btn_locator = ("xpath", '//button[contains(@class, "btn-special")]')
    # 登录信息定位
    error_msg_locator = ("xpath", '//div[@class="form-error-info"]')
    # 登录权限信息定位
    invalid_msg_locator = ("xpath", '//div[@class="layui-layer-content"]')

    def get(self):
        """访问login页面"""
        self.driver.get(self.url)
        # 这里return self 可以实现链式调用
        return self


    def login(self, mobile, pwd):
        """登录操作"""
        # self.mobile_locator 查找用户名元素
        username_elem = self.driver.find_element(*self.mobile_locator)
        # 输入手机号
        username_elem.send_keys(mobile)
        # 定位密码
        pwd_elem = self.driver.find_element(*self.pwd_locator)
        # 输入密码
        pwd_elem.send_keys(pwd)
        # 提交
        login_btn_elem = self.driver.find_element(*self.login_btn_locator)
        login_btn_elem.click()
        return self

    def get_error_msg(self):
        """获取错误信息"""
        e = self.driver.find_element(*self.error_msg_locator)
        # 返回错误信息的text文本
        return e.text

    def get_invalid_msg(self):
        # e = self.driver.find_element(*self.invalid_msg_locator)
        e = self.wait_element_visible(self.invalid_msg_locator)
        # 返回元素信息的text文本
        return e.text
