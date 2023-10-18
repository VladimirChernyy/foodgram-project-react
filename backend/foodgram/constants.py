from enum import IntEnum


class CustomUserLimit(IntEnum):
    MAX_LEN_EMAIL_FIELD = 150
    MAX_LEN_USERNAME = 150
    MAX_LEN_FIRST_NAME = 150
    MAX_LEN_LAST_NAME = 150


class RecipeLimitAndValidate(IntEnum):
    DEFAULT = 0
    MAX_LEN_NAME = 100
    MIN_COOKING_TIME = 1
    MAX_COOKING_TIME = 2880


class AmountIngredientValidate(IntEnum):
    DEFAULT = 0
    MAX_AMOUNT_INGREDIENTS = 50
    MIN_AMOUNT_INGREDIENTS = 1


class IngredientLimit(IntEnum):
    MAX_LEN_NAME = 60
    MAX_LEN_MEASUREMENT_UNIT = 10
    INGREDIENT_TITLE = 10


class TagLimit(IntEnum):
    MAX_LEN_NAME = 60
    MAX_LEN_COLOR = 16


class CustomPaginatorPageSize(IntEnum):
    PAGE_SIZE = 6
