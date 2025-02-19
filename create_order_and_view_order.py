# Александр Волков, 26А-я когорта — Финальный проект. Инженер по тестированию плюс
import sender_stand_request
import data

# -----------Функции------------

# функция получения токена
def post_new_order_token():
    order_response = sender_stand_request.post_new_order(data.order_body)
    return order_response


# Функция позитивной проверки
def positive_assert(new_order_token):
    new_order_track = sender_stand_request.get_new_order_view(new_order_token)
    assert new_order_track.status_code == 200  # проверка кода ответа



def test_create_track_and_view_order():
    track = post_new_order_token() #  Сохранение токена в переменную
    positive_assert(track)