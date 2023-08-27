import pytest
import os.path


ROOT_DIR = os.path.dirname(__file__)
RESOURCES_DIR = os.path.abspath(os.path.join(ROOT_DIR, 'resources'))


@pytest.fixture()
def remove_csv():
    yield
    os.remove(os.path.join(RESOURCES_DIR, 'new_csv.csv'))

@pytest.fixture()
def remove_img_pdf():
    yield
    os.remove(os.path.abspath('0Im1.png'))

@pytest.fixture()
def remove_zip():
    yield
    os.remove(os.path.abspath('new_zip.zip'))