from project.exceptions import ToManyDifferentProducts, NotEnoughSpace
from project.entities.base_storage import BaseStorage


class Shop(BaseStorage):
    """Магазин"""

    def __init__(self, items: dict[str, int], capacity: int = 20):
        self.__max_unique = 5

        if sum(items.values()) > capacity:
            raise NotEnoughSpace
        if len(set(items.values())) > self.__max_unique:
            raise ToManyDifferentProducts

        super().__init__(items=items, capacity=capacity)

    def add(self, title: str, amount: int) -> None:
        """Увеличивает запас items с учетом лимита capacity и max_unique"""

        if title not in self._items:
            if self._get_unique_items_count() == self.__max_unique:
                raise ToManyDifferentProducts

        super().add(title=title, amount=amount)
