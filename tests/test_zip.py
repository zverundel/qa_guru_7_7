from .conftest import RESOURCES_DIR
import os.path, zipfile


def test_zip_file(remove_zip):
    with zipfile.ZipFile('new_zip.zip', 'w') as zf:
        zf.write(os.path.join(RESOURCES_DIR, 'file_example_XLSX_50.xlsx'), 'file_example_XLSX_50.xlsx')
        zf.write(os.path.join(RESOURCES_DIR, 'docs-pytest-org-en-latest.pdf'), 'docs-pytest-org-en-latest.pdf')
        zf.write(os.path.join(RESOURCES_DIR, 'file_example_XLS_10.xls'), 'file_example_XLS_10.xls')


    with zipfile.ZipFile('new_zip.zip', 'r') as zf:
        for file in zf.namelist():
            print(file)

    assert zf.namelist() == ['file_example_XLSX_50.xlsx', 'docs-pytest-org-en-latest.pdf', 'file_example_XLS_10.xls']
