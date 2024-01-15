from pages.interactions_page import SortablePage, SelectablePage, ResizablePage


class TestInteractions:
    class TestSortablePage:
        def test_sortable(self, driver):
            sortable_page = SortablePage(driver, 'https://demoqa.com/sortable')
            sortable_page.open()
            list_before, list_after = sortable_page.change_list_order()
            grid_before, grid_after = sortable_page.change_grid_order()
            assert list_before != list_after, 'the order of the list has not been changed'
            assert grid_before != grid_after, 'the order of the grid has not been changed'

    class TestSelectablePage:
        def test_sortable(self, driver):
            selectable_page = SelectablePage(driver, 'https://demoqa.com/selectable')
            selectable_page.open()
            list_select = selectable_page.select_list_item()
            grid_select = selectable_page.select_grid_item()
            assert len(list_select) > 0, "no list object were selected"
            assert len(grid_select) > 0, "no grid object were selected"

    class TestResizablePage:
        def test_resizable(self, driver):
            resizable_page = ResizablePage(driver, 'https://demoqa.com/resizable')
            resizable_page.open()
            max_box, min_box = resizable_page.change_size_resizable_box()
            max_resizable, min_resizable = resizable_page.change_size_resizable()
            assert ('400px', '300px') == max_box, "maximum size not equal to '400px', '300px'"
            assert ('150px', '150px') == min_box, "minimum size not equal to '150px', '150px'"
            assert min_resizable != max_resizable, "resizable has not been changed"
