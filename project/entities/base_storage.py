from project.exceptions import NotEnoughSpace, NotFound, NotEnoughProduct
from project.entities.storage import Storage


class BaseStorage(Storage):

    def __init__(self, capacity: int, items: dict[str, int]):
        self._items = items
        self.__capacity = capacity

    def add(self, title: str, amount: int) -> None:
        """Увеличивает запас items с учетом лимита capacity"""
        if self._get_free_space() < amount:
            raise NotEnoughSpace

        if title in self._items:
            self._items[title] += amount
        else:
            self._items[title] = amount

    def remove(self, title: str, amount: int) -> None:
        """Уменьшает запас items, но не ниже 0"""
        if self._items.get(title, None) is None:
            raise NotFound

        if self._items.get(title) < amount:
            raise NotEnoughProduct

        self._items[title] -= amount

        if self._items.get(title) == 0:
            self._items.pop(title)

    def _get_free_space(self) -> int:
        """Возвращает количество свободных мест"""
        result = self.__capacity - sum(self._items.values())
        return [result if result else 0][0]

    def get_items(self) -> str:
        """Возвращает содержание склада в словаре {товар: количество}"""
        return "\n".join([f"{k}: {v}" for k, v in self._items.items()])

    def _get_unique_items_count(self) -> int:
        """Возвращает количество уникальных товаров"""
        return len(set(self._items.keys()))
