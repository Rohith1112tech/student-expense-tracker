from datetime import date, datetime


class ValidationError(ValueError):
    """Raised when user input fails validation."""


def read_non_empty(value, field_name):
    value = value.strip()
    if not value:
        raise ValidationError(f"{field_name} cannot be empty.")
    return value


def read_amount(value):
    try:
        amount = float(value)
    except ValueError as exc:
        raise ValidationError("Amount must be a valid number.") from exc

    if amount <= 0:
        raise ValidationError("Amount must be greater than zero.")
    return round(amount, 2)


def read_date(value, allow_blank=False):
    value = value.strip()
    if allow_blank and not value:
        return date.today().isoformat()

    try:
        parsed = datetime.strptime(value, "%Y-%m-%d").date()
        return parsed.isoformat()
    except ValueError as exc:
        raise ValidationError("Date must use YYYY-MM-DD format.") from exc


def validate_month(month):
    try:
        datetime.strptime(month, "%Y-%m")
    except ValueError as exc:
        raise ValidationError("Month must use YYYY-MM format.") from exc
    return month
