import pytest
import allure

from base.base_driver import init_driver
from page.page import Page
from base.base_analyze import analyze_with_file


class TestMms:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.parametrize("args", analyze_with_file("mms_data", "test_mms1"))
    @allure.severity('critical')
    def test_mms1(self, args):
        # receive = "13718701752"
        # input = "hello"
        receive = args["receive"]
        msg = args["msg"]
        self.page.show_mms.new_mms_button()
        self.page.send_mms.receive_msg(receive)
        self.page.send_mms.input_msg(msg)
        self.page.send_mms.send_button()
        assert self.page.success_mms.find_msg() == msg

    @pytest.mark.parametrize("args", analyze_with_file("mms_data", "test_mms2"))
    @allure.severity('blocker')
    def test_mms2(self, args):
        # receive = "13718701752"
        # input = "hello"
        receive = args["receive"]
        msg = args["msg"]
        self.page.show_mms.new_mms_button()
        self.page.send_mms.receive_msg(receive)
        self.page.send_mms.input_msg(msg)
        self.page.send_mms.send_button()
        assert self.page.success_mms.find_msg() == msg
