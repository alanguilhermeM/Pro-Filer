from pro_filer.actions.main_actions import show_details  # NOQA


def test_show_details(capsys):
    context = {
        "base_path": "/home/trybe/Downloads/Trybe_logo.png"
    }

    show_details(context)

    captured = capsys.readouterr()
    expected_output = (
        "File name: Trybe_logo.png\n"
        "File size in bytes: 22438\n"
        "File type: file\n"
        "File extension: .png\n"
        "Last modified date: 2023-06-13\n"
    )

    assert captured.out == expected_output
