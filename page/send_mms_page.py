import allure
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class SendMmsPage(BaseAction):
    receive_tel = By.XPATH,"//*[@text='接收者']"
    input_tel = By.XPATH, "//*[@text='键入信息']"
    send_msg = By.XPATH, "//*[@content-desc='发送']"

    @allure.step(title="输入接收人")
    def receive_msg(self,text):
        allure.attach("接收人", text)
        self.input(self.receive_tel,text)

    @allure.step(title="输入信息")
    def input_msg(self,text):
        # 附件，一个提示信息 内容 类型（如果是文字默认可以省略）
        allure.attach("信息", text)
        self.input(self.input_tel,text)

        # 本地会保留图片
        # self.driver.get_screenshot_as_file("./xx.png")
        # with open("./xx.png",'rb') as f:
        #     allure.attach('截图',f.read(), allure.attach_type.PNG)

        # 本地不会保留图片
        allure.attach('截图', self.driver.get_screenshot_as_png(), allure.attach_type.PNG)

    @allure.step(title="点击发送")
    def send_button(self):
        self.click(self.send_msg)

