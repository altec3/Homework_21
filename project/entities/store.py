from project.entities.base_storage import BaseStorage
from project.exceptions import NotEnoughSpace


class Store(BaseStorage):
    """Склад"""

    def __init__(self, items: dict, capacity: int = 100):
        if sum(items.values()) > capacity:
            raise NotEnoughSpace
        super().__init__(items=items, capacity=capacity)
