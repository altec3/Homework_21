from project.exceptions import InvalidRequest


class Request:

    def __init__(self, user_input: list):
        if len(user_input) < 4:
            raise InvalidRequest

        self._product = user_input[0]
        self._amount = int(user_input[1])
        self._where_from = user_input[2]
        self._to = user_input[3]

        # Проверка пунктов доставки
        if self._where_from == self._to:
            raise InvalidRequest

    @property
    def where_from(self):
        return self._where_from

    @property
    def to(self):
        return self._to

    @property
    def amount(self):
        return self._amount

    @property
    def product(self):
        return self._product
