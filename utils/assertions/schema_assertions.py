from jsonschema import Draft7Validator, SchemaError, ValidationError

from utils.file_reader import read_schema_file
from utils.logger import logger

log = logger('schema_assertions')


def schema_is_valid(response, schema_file_name, file_folder):
    array_schema = read_schema_file(f'{schema_file_name}.json', file_folder)
    validator = Draft7Validator(array_schema)
    try:
        validator.validate(response.as_dict)
        log.info("Schema validated successfully")
        return True
    except SchemaError:
        log.error("\nThere is an error with the schema. Please check the file: " + schema_file_name)
    except ValidationError as e:

        log.error(e)
