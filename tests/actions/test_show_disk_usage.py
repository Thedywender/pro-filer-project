from pro_filer.actions.main_actions import show_disk_usage  # NOQA


def test_show_disk_usage_success(mock_files, capsys):
    show_disk_usage(mock_files)

    captured = capsys.readouterr()
    expected_output = f"""'test.py':{''.ljust(60)} 12 (60%)
'test.py':{''.ljust(60)} 8 (40%)
Total size: 20\n"""

    assert captured.out == expected_output
