from pages.alerts_frame_window_page import BrowserWindowsPage


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