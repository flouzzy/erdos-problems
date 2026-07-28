import pytest
import os
import tempfile
from unittest.mock import patch, call
from read_all import print_file_contents, main

def test_print_file_contents_success(capsys):
    with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.py') as temp:
        temp.write("print('hello')")
        temp_name = temp.name

    try:
        result = print_file_contents(temp_name)
        assert result is True

        captured = capsys.readouterr()
        filename_only = temp_name.split('/')[-1]
        assert f"--- {filename_only} ---" in captured.out
        assert "print('hello')" in captured.out
    finally:
        os.unlink(temp_name)

def test_print_file_contents_file_not_found(capsys):
    result = print_file_contents("nonexistent_file.py")
    assert result is False

    captured = capsys.readouterr()
    assert "File not found: nonexistent_file.py" in captured.out

@patch('read_all.print_file_contents')
def test_main(mock_print_file_contents):
    main()
    expected_calls = [
        call("inprogress/04-Erdos-Gyarfas/test_generate_erdos_gyarfas_proof.py"),
        call("inprogress/04-Erdos-Gyarfas/test_generate_proof.py")
    ]
    mock_print_file_contents.assert_has_calls(expected_calls, any_order=True)
