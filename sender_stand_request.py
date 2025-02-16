# Импорт настроек из модуля configuration, который содержит параметры конфигурации, такие как URL сервиса
import configuration

# Импорт библиотеки requests для выполнения HTTP-запросов
import requests

# Импорт данных запроса из модуля data, в котором определены заголовки и тело запроса
import data


# Создаем заказ
def post_new_order(order_body):
    order_token = requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,  # подставляем полный url
                                json=order_body,  # тут тело
                                headers=data.headers)  # а здесь заголовки
    return order_token.json()['track']


# проверяем информацию о заказе
def get_new_order_view(order_token):
    request_body = requests.get(configuration.URL_SERVICE + configuration.CHECKING_THE_ORDER_BY_TRACK + str(order_token),
                                headers=data.headers)
    return request_body


