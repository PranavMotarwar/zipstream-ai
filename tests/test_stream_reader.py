from zipstream_ai import ZipStreamReader

def test_list_files():
    reader = ZipStreamReader("tests/test.zip")
    files = reader.list_files()
    assert isinstance(files, list)