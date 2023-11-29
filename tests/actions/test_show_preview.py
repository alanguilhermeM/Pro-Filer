from pro_filer.actions.main_actions import show_preview  # NOQA

e = "First 5 files: ['src/__init__.py', 'src/app.py', 'src/utils/__init__.py']"


def test_show_preview(capsys):
    context = {
        "all_files": [
            "src/__init__.py",
            "src/app.py",
            "src/utils/__init__.py"
        ],
        "all_dirs": [
            "src",
            "src/utils"
        ]
    }
    show_preview(context)

    captured = capsys.readouterr().out.split('\n')

    assert captured[0] == "Found 3 files and 2 directories"
    assert captured[1] == e
    assert captured[2] == "First 5 directories: ['dir']"


def test_show_preview_with_no_files(capsys):
    context = {
        "all_files": [],
        "all_dirs": []
    }
    show_preview(context)

    captured = capsys.readouterr()
    expected_output = "Found 0 files and 0 directories\n"
    assert captured.out == expected_output
