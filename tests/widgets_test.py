from pages.widgets_page import AccordianPage


class TestWidgets:
    class TestWidgetsPage:
        def test_accordian(self, driver):
            widgets_page = AccordianPage(driver, 'https://demoqa.com/accordian')
            widgets_page.open()
            first_title, first_content = widgets_page.check_accordian('first')
            second_title, second_content = widgets_page.check_accordian('second')
            third_title, third_content = widgets_page.check_accordian('third')
            assert first_title == 'What is Lorem Ipsum?' and first_content > 0, 'Incorrect title or missing text'
            assert second_title == 'Where does it come from?' and second_content > 0, 'Incorrect title or missing text'
            assert third_title == 'Why do we use it?' and third_content > 0, 'Incorrect title or missing text'