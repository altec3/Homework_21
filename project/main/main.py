import logging

from project.entities.courier import Courier
from project.entities.request import Request
from project.entities.shop import Shop
from project.entities.store import Store
from project.exceptions import InvalidRequest, BaseError, NotEnoughSpace, ToManyDifferentProducts

store = Store(items={
    "машинки": 25,
    "конфеты": 13,
    "леденцы": 18,
    "мячи": 18,
    "лыжи": 6,
    "карандаши": 19,
})
shop = Shop(items={
    "машинки": 5,
    "конфеты": 3,
    "леденцы": 7,
    "ролики": 2,
})
storages = {
    "склад": store,
    "магазин": shop,
}


def main():

    while True:
        for storage in storages:
            print(f"\nСодержимое {storage}а:\n{storages[storage].get_items()}")

        user_input = [input(f"\nЧто везем?\n-> ").lower().strip(),
                      input(f"Сколько?\n-> ").strip(),
                      input(f"Откуда?\n-> ").lower().strip(),
                      input(f"Куда?\n-> ").lower().strip(),
                      ]
        if "стоп" in user_input or "stop" in user_input:
            break

        try:
            request = Request(user_input)
            print(f"Доставить {request.amount} {request.product} из {request.where_from} в {request.to}")
        except ValueError as error:
            logging.debug(error)
            print("Введите корректное количество товара (число)")
            continue

        try:
            courier = Courier(request=request, storages=storages)
        except InvalidRequest as error:
            logging.debug(error.message)
            print(f"Введите корректные точки начала и конца маршрута {tuple(storages.keys())}")
            continue

        try:
            courier.movie()
        except NotEnoughSpace as error:
            print(error.message)
            courier.cancel()
            continue
        except ToManyDifferentProducts as error:
            print(error.message)
            courier.cancel()
            continue
        except BaseError as error:
            print(error.message)
            continue


if __name__ == "__main__":
    main()
