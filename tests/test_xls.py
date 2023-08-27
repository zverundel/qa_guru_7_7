import xlrd
from .conftest import RESOURCES_DIR
import os.path

# TODO оформить в тест, добавить ассерты и использовать универсальный путь

def test_xls_file():
    book = xlrd.open_workbook(os.path.join(RESOURCES_DIR, 'file_example_XLS_10.xls'))
    sheet = book.sheet_by_index(0)
    rows = []

    print(f'Количество листов {book.nsheets}')
    print(f'Имена листов {book.sheet_names()}')
    print(f'Количество колонок  {sheet.ncols}')
    print(f'Количество строк    {sheet.nrows}')
    print(f'Пересечение строки и столбца {sheet.cell_value(rowx=3, colx=2)}')

    for rx in range(sheet.nrows):
        rows.append(sheet.row(rx))
        print(sheet.row(rx))

    assert book.nsheets == 1
    assert book.sheet_names()[0] == 'Sheet1'
    assert sheet.ncols == 8
    assert sheet.nrows == 10
    assert sheet.cell_value(rowx=3, colx=2) == 'Gent'
    assert len(rows) == 10