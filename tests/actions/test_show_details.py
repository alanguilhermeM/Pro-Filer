from pro_filer.actions.main_actions import show_details  # NOQA


def test_show_details(capsys):
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
        "Last modified date: 2023-11-28\n"
    )

    assert captured.out == expected_output


def test_show_details_with_no_extension(capsys):
    context = {
        "base_path": "pro_filer"
    }

    show_details(context)

    captured = capsys.readouterr()
    expected_output = (
        "File name: pro_filer\n"
        "File size in bytes: 4096\n"
        "File type: directory\n"
        "File extension: [no extension]\n"
        "Last modified date: 2023-11-28\n"
    )

    assert captured.out == expected_output


def test_not_existing_show_details(capsys):
    context = {
        "base_path": "/home/trybe/????"
    }

    show_details(context)

    captured = capsys.readouterr()

    assert captured.out == "File '????' does not exist\n"
