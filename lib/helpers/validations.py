def validate_int(value, field_name="Value"):
    try:
        return int(value)
    except (ValueError, TypeError):
        raise ValueError(f"{field_name} must be a valid integer.")


def validate_non_empty_string(value, field_name="Value"):
    if not value or not isinstance(value, str):
        raise ValueError(f"{field_name} must be a non-empty string.")
    return value


def validate_choice(value, choices, field_name="Value"):
    if value not in choices:
        raise ValueError(
            f"{field_name} must be one of: {', '.join(choices)}"
        )
    return value
