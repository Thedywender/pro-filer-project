from pro_filer.actions.main_actions import show_preview  # NOQA


def test_show_preview_no_files_or_dirs(capsys):
    context = {"all_files": [], "all_dirs": []}
    show_preview(context)
    captured = capsys.readouterr()
    assert captured.out == "Found 0 files and 0 directories\n"


def test_show_preview_with_files_and_dirs(capsys):
    context = {
        "all_files": [
            "src/__init__.py",
            "src/app.py",
            "src/utils/__init__.py",
        ],
        "all_dirs": ["src", "src/utils"],
    }
    show_preview(context)
    captured = capsys.readouterr()
    expected_output = (
        "Found 3 files and 2 directories\n"
        "First 5 files: ['src/__init__.py', 'src/app.py', "
        "'src/utils/__init__.py']\n"
        "First 5 directories: ['src', 'src/utils']\n"
    )
    assert captured.out == expected_output
