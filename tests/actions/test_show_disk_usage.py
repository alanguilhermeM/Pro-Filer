from pro_filer.actions.main_actions import show_disk_usage  # NOQA


def create_test_files(tmp_path):
    src_dir = tmp_path / "src"
    src_dir.mkdir()
    (src_dir / "app.py").write_text("a" * 2849)
    (src_dir / "__init__.py").write_text("")


def test_show_disk_usage(tmp_path, capsys):
    create_test_files(tmp_path)

    context = {"all_files": [str(tmp_path / "src" / "app.py"),
                             str(tmp_path / "src" / "__init__.py")]}
    show_disk_usage(context)

    captured = capsys.readouterr().out.split('\n')
    assert "Total size: 2849" in captured


def test_not_existing_show_disk_usage(capsys):
    context = {
        "all_files": []
    }

    show_disk_usage(context)

    captured = capsys.readouterr()

    assert captured.out == "Total size: 0\n"


def get_file_info(captured):
    file_lns = [line for line in captured.split("\n") if line.startswith("'")]
    return [
        (
            line.split(":")[0].strip("'").strip(),
            int(line.split(":")[1].split("(")[0].strip()),
        )
        for line in file_lns
    ]


def test_show_disk_usage_sorted_output(tmp_path, capsys):
    create_test_files(tmp_path)

    context = {
        "all_files": [
            str(tmp_path / "src" / "app.py"),
            str(tmp_path / "src" / "__init__.py"),
        ]
    }

    show_disk_usage(context)

    captured = capsys.readouterr().out

    file_info = get_file_info(captured)

    assert file_info == sorted(file_info, key=lambda x: x[1], reverse=True)
    assert "Total size:" in captured
