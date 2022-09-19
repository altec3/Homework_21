from project.entities.base_storage import BaseStorage
from project.entities.request import Request
from project.exceptions import InvalidRequest


class Courier:
    def __init__(self, request: Request, storages: dict[str, BaseStorage]):
        self._storages = storages
        self._product = request.product
        self._amount = request.amount
        self._from = request.where_from
        self._to = request.to

        # Проверка пунктов доставки
        if self._from not in storages or self._to not in storages:
            raise InvalidRequest

    def movie(self):
        self._storages[self._from].remove(title=self._product, amount=self._amount)
        print(f"\nКурьер забрал {self._amount} {self._product} со {self._from}")
        print(f"Курьер везет {self._amount} {self._product} со {self._from} в {self._to}")

        self._storages[self._to].add(self._product, self._amount)
        print(f"Курьер доставил {self._amount} {self._product} в {self._to}")

    def cancel(self):
        self._storages[self._from].add(title=self._product, amount=self._amount)
        print(f"Курьер вернул {self._amount} {self._product} на {self._from}")
