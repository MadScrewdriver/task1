import re


# Allowed: letters, digits, space and . , ' ! ? : -
TEXT_PATTERN = re.compile(r"\w[\w .,'!?:-]{0,63}")


def validate_text(field, value):
    if not isinstance(value, str) or not TEXT_PATTERN.fullmatch(value):
        raise ValueError(f'{field}: invalid characters or length')

    return value
