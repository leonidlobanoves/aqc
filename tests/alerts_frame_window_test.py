from pages.alerts_frame_window_page import BrowserWindowsPage, AlertsPage


class TestAlertsFrameWindow:
    class TestBrowserWindow:

        def test_new_tab(self, driver):
            new_tab_page = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
            new_tab_page.open()
            text_result = new_tab_page.check_opened_new_tab()
            assert text_result == 'This is a sample page', "the new tab has not opened or an incorrect tab has opened"



        def test_new_window(self, driver):
            new_tab_window = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
            new_tab_window.open()
            text_result = new_tab_window.check_opened_new_window()
            assert text_result == 'This is a sample page', "the new window has not opened or an incorrect window has opened"


    class TestAlertsPage:
        def test_see_alert(self, driver):
            alerts_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alerts_page.open()
            alert_text = alerts_page.check_see_alert()
            assert alert_text == 'You clicked a button'

        def test_alert_appear_5_sec(self, driver):
            alerts_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alerts_page.open()
            alert_text = alerts_page.check_alert_appear_5_sec()
            assert alert_text == 'This alert appeared after 5 seconds'

        def test_alert_confirm(self, driver):
            alerts_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alerts_page.open()
            alert_text = alerts_page.check_confirm_alert()
            assert alert_text == 'You selected Ok'

        def test_alert_prompt(self, driver):
            alerts_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alerts_page.open()
            text, alert_text = alerts_page.check_prompt_alert()
            assert alert_text == f'You entered {text}'