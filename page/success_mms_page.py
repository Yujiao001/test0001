import allure
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class SuccessMmsPage(BaseAction):

    succ_msg = By.ID,"com.android.mms:id/text_view"

    @allure.step(title="确认发送成功")
    def find_msg(self):
        return self.last_element_text(self.succ_msg)