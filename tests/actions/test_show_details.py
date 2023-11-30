from pro_filer.actions.main_actions import show_details  # NOQA
from datetime import datetime


def test_show_details(capsys):
    current_date = datetime.now().strftime("%Y-%m-%d")
    context = {
        "base_path": "pro_filer/__init__.py"
    }

    show_details(context)

    captured = capsys.readouterr()
    expected_output = (
        "File name: __init__.py\n"
        "File size in bytes: 0\n"
        "File type: file\n"
        "File extension: .py\n"
        f"Last modified date: {current_date}\n"
    )

    assert captured.out == expected_output


def test_show_details_with_no_extension(capsys, tmp_path):
    current_date = datetime.now().strftime("%Y-%m-%d")

    file = tmp_path / "tmp_file"
    file.write_text("content")

    context = {
        "base_path": str(file)
    }

    show_details(context)

    captured = capsys.readouterr()
    expected_output = (
        "File name: tmp_file\n"
        "File size in bytes: 7\n"
        "File type: file\n"
        "File extension: [no extension]\n"
        f"Last modified date: {current_date}\n"
    )

    assert captured.out == expected_output


def test_not_existing_show_details(capsys):
    context = {
        "base_path": "/home/trybe/????"
    }

    show_details(context)

    captured = capsys.readouterr()

    assert captured.out == "File '????' does not exist\n"
