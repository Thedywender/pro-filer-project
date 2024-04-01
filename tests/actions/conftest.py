import pytest
from unittest.mock import Mock


@pytest.fixture(autouse=True)
def mock_files(tmp_path, monkeypatch):
    file = tmp_path / "test.py"
    file.write_text("12345678")

    file_2 = tmp_path / "test2.py"
    file_2.write_text("123456789012")

    file_str = str(file)
    file_str_2 = str(file_2)

    mock_function = "pro_filer.actions.main_actions._get_printable_file_path"
    mock_result = Mock(return_value="test.py")
    monkeypatch.setattr(mock_function, mock_result)

    context = {"all_files": [file_str, file_str_2]}
    return context
