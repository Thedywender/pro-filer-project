import pytest
from pro_filer.actions.main_actions import find_duplicate_files  # NOQA
from unittest.mock import patch


def test_find_duplicate_files_no_duplicates(tmp_path):
    file1 = tmp_path / "file1.txt"
    file1.write_text("abcdef")

    file2 = tmp_path / "file2.txt"
    file2.write_text("ghijkl")

    context = {"all_files": [str(file1), str(file2)]}

    assert find_duplicate_files(context) == []


def test_find_duplicate_files_with_duplicates(tmp_path):
    file1 = tmp_path / "file1.txt"
    file1.write_text("abcdef")

    file2 = tmp_path / "file2.txt"
    file2.write_text("abcdef")

    context = {"all_files": [str(file1), str(file2)]}

    assert find_duplicate_files(context) == [(str(file1), str(file2))]


def test_find_duplicate_files_file_not_found():
    context = {"all_files": ["/path/to/nonexistent/file"]}

    with pytest.raises(ValueError):
        find_duplicate_files(context)


def test_find_duplicate_files_file_not_found(tmp_path):
    file1 = tmp_path / "file1.txt"
    file1.write_text("abcdef")

    context = {"all_files": [str(file1), "/path/to/nonexistent/file"]}

    with pytest.raises(ValueError):
        find_duplicate_files(context)
