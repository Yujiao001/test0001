import allure
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class ShowMmsPage(BaseAction):
    new_mms = By.ID,"com.android.mms:id/action_compose_new"

    @allure.step(title="点击新建信息")
    def new_mms_button(self):
        self.click(self.new_mms)