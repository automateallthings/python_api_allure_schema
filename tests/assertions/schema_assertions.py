from jsonschema import Draft7Validator, SchemaError, ValidationError

from utils.file_reader import read_file


def schema_is_valid(schema, schema_file_name):
    array_schema = read_file(f'{schema_file_name}.json')
    validator = Draft7Validator(array_schema)
    try:
        validator.validate(schema)
        return True
    except SchemaError:
        # UPDATE WITH LOGGER
        print("\nThere is an error with the schema. Please check the file: " + schema_file_name)

    except ValidationError as e:
        # UPDATE WITH LOGGER
        print(e)
