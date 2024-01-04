from pages.alerts_frame_window_page import BrowserWindowsPage, AlertsPage, FramesPage, NestedFramesPage


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
            assert alert_text == 'You clicked a button', "Alert did not show up"

        def test_alert_appear_5_sec(self, driver):
            alerts_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alerts_page.open()
            alert_text = alerts_page.check_alert_appear_5_sec()
            assert alert_text == 'This alert appeared after 5 seconds', "Alert did not show up"

        def test_alert_confirm(self, driver):
            alerts_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alerts_page.open()
            alert_text = alerts_page.check_confirm_alert()
            assert alert_text == 'You selected Ok', "Alert did not show up"

        def test_alert_prompt(self, driver):
            alerts_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alerts_page.open()
            text, alert_text = alerts_page.check_prompt_alert()
            assert alert_text == f'You entered {text}', "Alert did not show up"


    class TestFramesPage:
        def test_frames(self, driver):
            frame_page = FramesPage(driver, 'https://demoqa.com/frames')
            frame_page.open()
            result_frame1 = frame_page.check_frame('frame1')
            result_frame2 = frame_page.check_frame('frame2')
            assert result_frame1 == ['This is a sample page', '500px', '350px'], 'The frame does not exist'
            assert result_frame2 == ['This is a sample page', '100px', '100px'], 'The frame does not exist'

    class TestNestedFrames:
        def test_nested_frames(self, driver):
            nested_frame_page = NestedFramesPage(driver, 'https://demoqa.com/nestedframes')
            nested_frame_page.open()
            parent_text, child_text = nested_frame_page.check_nested_frames()
            assert parent_text == 'Parent frame', 'Nested frame does not exist'
            assert child_text == 'Child Iframe', 'Nested frame does not exist'