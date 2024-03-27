from unittest.mock import patch
from pro_filer.actions.main_actions import show_details  # NOQA


def test_show_details_withou_path(capsys):
    context = {"base_path": "/home/trybe/????"}
    show_details(context)
    captured = capsys.readouterr()
    assert captured.out == "File '????' does not exist\n"


def test_show_details_with_valid_path(capsys):
    context = {"base_path": "/home/trybe/Downloads/Trybe_logo.png"}

    with patch("os.path.exists", return_value=True):
        with patch("os.path.getsize", return_value=22438):
            with patch("os.path.isdir", return_value=False):
                with patch("os.path.getmtime", return_value=1689315018.0):
                    show_details(context)

    captured = capsys.readouterr()
    expected_output = (
        "File name: Trybe_logo.png\n"
        "File size in bytes: 22438\n"
        "File type: file\n"
        "File extension: .png\n"
        "Last modified date: 2023-07-14\n"
    )
    assert captured.out == expected_output
