from django.core.exceptions import ValidationError


CATEGORIES = ['Mexican', 'Asian', 'American', 'Whatever']


def validate_email(value):
    if '.edu' in value:
        raise ValidationError('We do not accept edu emails')


def validate_category(value):
    if value not in CATEGORIES and value.capitalize() not in CATEGORIES:
        raise ValidationError(f"{value} is not a valid category")
