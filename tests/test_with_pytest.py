"""This is the starting test file app"""

from app import print_hello_name


def test_always_passes():
    """This always passes"""
    assert True


def test_hello_world_print(capsys):
    """You have to make this test pass by changing World to Keith"""\

    print_hello_name('Keith')
    # This is how we capture the terminal output after running the print command.
    # Out is the console ouptput and err is an error
    out, err = capsys.readouterr()
    assert out == 'Hello Keith\n'
    assert err == ''
