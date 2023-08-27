import pypdf
import os.path
from .conftest import RESOURCES_DIR


# TODO оформить в тест, добавить ассерты и использовать универсальный путь


def test_pdf_file(remove_img_pdf):
    reader = pypdf.PdfReader(os.path.join(RESOURCES_DIR, 'docs-pytest-org-en-latest.pdf'))
    number_of_pages = len(reader.pages)
    first_page = reader.pages[0]
    text = first_page.extract_text()
    count = 0
    for image_file in first_page.images:
        with open(str(count) + image_file.name, 'wb') as fp:
            fp.write(image_file.data)
            count += 1
    print(number_of_pages)
    print(first_page)
    print(text)

    assert number_of_pages == 412
    assert text == ('pytest Documentation\n'
                    'Release 0.1\n'
                    'holger krekel, trainer and consultant, https://merlinux.eu/\n'
                    'Jul 14, 2022')
    assert count == 1
    assert os.path.isfile(os.path.abspath('0Im1.png'))