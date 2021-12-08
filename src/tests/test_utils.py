from src.utils.remove_special_caracters import remove_special_caracters
from src.utils.check_file import check_file, read_file


def test_remove_special_caracters():
    text = "[2, 2, 3, 1, 0]"
    response = remove_special_caracters(text)
    assert type(response) == str
    assert response == "2,2,3,1,0"


def test_file_is_exists():
    response = check_file()
    assert response == True

def test_read_file():
    """
    Check if it has content in the file.
    """
    response = read_file()
    assert type(response) == list
    assert len(response) > 0
