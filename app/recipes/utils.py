from django.core.exceptions import ValidationError


def check_required_arguments(func):
    def wrapper(*args, **kwargs):
        if not all(kwargs.values()):
            vals = kwargs.keys()
            suffix = "{}, " * len(vals)
            raise ValidationError("missing required arguments. Required arguments: " + suffix[:-2].format(*vals))

        return func(*args, **kwargs)

    return wrapper
