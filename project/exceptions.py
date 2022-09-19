class BaseError(Exception):
    message = "Неожиданная ошибка"


class NotFound(BaseError):
    message = "Товар отсутствует на складе"


class NotEnoughSpace(BaseError):
    message = "Недостаточно места на складе"


class NotEnoughProduct(BaseError):
    message = "Недостаточно товара на складе"


class ToManyDifferentProducts(BaseError):
    message = "Исчерпан лимит товаров"


class InvalidRequest(BaseError):
    message = "Неправильный запрос. Попробуйте снова"
