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
            "src/utils/helper.py",
            "src/utils/utils.py",
            "src/utils/extra.py",
        ],
        "all_dirs": [
            "src",
            "src/utils",
            "src/extra",
            "src/helper",
            "src/utils/extra",
            "src/utils/helper",
        ],
    }
    show_preview(context)
    captured = capsys.readouterr()
    expected_output = (
        "Found 6 files and 6 directories\n"
        "First 5 files: ['src/__init__.py', 'src/app.py', 'src/utils/__init__.py', 'src/utils/helper.py', 'src/utils/utils.py']\n"
        "First 5 directories: ['src', 'src/utils', 'src/extra', 'src/helper', 'src/utils/extra']\n"
    )
    assert captured.out == expected_output
