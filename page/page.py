from page.send_mms_page import SendMmsPage
from page.show_mms_page import ShowMmsPage
from page.success_mms_page import SuccessMmsPage


class Page:
    def __init__(self,driver):
        self.driver = driver
        self.page = Page

    @property
    def show_mms(self):
        return ShowMmsPage(self.driver)

    @property
    def send_mms(self):
        return SendMmsPage(self.driver)

    @property
    def success_mms(self):
        return SuccessMmsPage(self.driver)
