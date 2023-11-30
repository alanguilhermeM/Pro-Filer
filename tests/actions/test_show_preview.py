from pro_filer.actions.main_actions import show_preview  # NOQA
from unittest.mock import patch, Mock

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
    assert captured[2] == "First 5 directories: ['src', 'src/utils']"


def test_show_preview_with_no_files():
    context = {"all_files": [], "all_dirs": []}

    expected_output = "Found 0 files and 0 directories"
    mock = Mock(side_effect=lambda *args, **kwargs: print(*args, **kwargs))

    with patch("pro_filer.actions.main_actions.print", mock):
        show_preview(context)

    mock.assert_called_with(expected_output)
