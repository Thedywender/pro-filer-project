from pro_filer.actions.main_actions import show_details  # NOQA
from datetime import date


def test_show_details_withou_path(capsys):
    context = {"base_path": "/home/trybe/????"}
    show_details(context)
    captured = capsys.readouterr()
    assert captured.out == "File '????' does not exist\n"


def test_show_details_with_valid_path(capsys, tmp_path):
    file_path = tmp_path / "Trybe_logo.png"
    file_path.write_text("Dummy content")

    context = {"base_path": str(file_path)}

    show_details(context)

    captured = capsys.readouterr()
    expected_output = (
        f"File name: Trybe_logo.png\n"
        f"File size in bytes: {file_path.stat().st_size}\n"
        f"File type: file\n"
        f"File extension: .png\n"
        f"Last modified date: {date.fromtimestamp(file_path.stat().st_mtime).isoformat()}\n"
    )
    assert captured.out == expected_output


def test_show_details_with_file_without_extension(capsys, tmp_path):
    file_path = tmp_path / "Trybe_logo"
    file_path.write_text("Dummy content")

    context = {"base_path": str(file_path)}

    show_details(context)

    captured = capsys.readouterr()
    expected_output = (
        f"File name: Trybe_logo\n"
        f"File size in bytes: {file_path.stat().st_size}\n"
        f"File type: file\n"
        f"File extension: [no extension]\n"
        f"Last modified date: {date.fromtimestamp(file_path.stat().st_mtime).isoformat()}\n"
    )
    assert "[no extension]" in captured.out
