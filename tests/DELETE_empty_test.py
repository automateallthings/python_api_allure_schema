from utils.file_reader import read_file


def test_empty_one():
    schemaFile = read_file('product_associated_to_account.json')
    print(schemaFile)
