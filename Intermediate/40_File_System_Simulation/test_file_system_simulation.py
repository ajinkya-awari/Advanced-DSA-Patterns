import pytest
from file_system_simulation import FileSystem

@pytest.fixture
def fs():
    f = FileSystem()
    f.mkdir("/home/user")
    return f

def test_file_operations(fs):
    fs.write_file("/home/user/test.txt", "Hello World")
    assert fs.read_file("/home/user/test.txt") == "Hello World"
    assert fs.get_file_hash("/home/user/test.txt") is not None

def test_directory_listing(fs):
    fs.write_file("/home/user/a.txt", "a")
    fs.mkdir("/home/user/docs")
    contents = fs.list_dir("/home/user")
    assert contents == ["a.txt", "docs"]

def test_not_found(fs):
    with pytest.raises(FileNotFoundError):
        fs.read_file("/ghost.txt")
