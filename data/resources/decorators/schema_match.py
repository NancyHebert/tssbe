import falcon
from cerberus import Validator, errors


def schema_match(schema):
    def decorator(func):
        def func_wrapper(*args, **kwargs):
            v = Validator(schema)
            if not v.validate(kwargs, schema):
                raise falcon.HTTPBadRequest('Type Error', v.errors)
            return func(*args, **kwargs)
        return func_wrapper
    return decorator
