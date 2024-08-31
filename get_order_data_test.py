# Алексей Решетов, 20а-я когорта — Финальный проект. Инженер по тестированию плюс
import sender_stand_request
import Data

def get_track_number():
    get_track = sender_stand_request.post_new_order(Data.order_body)
    track_number = get_track.json()["track"]
    track_number = str(track_number)
    return track_number

def test_positive_assert_code_200():
    track_number = get_track_number()
    order_data_response = sender_stand_request.get_order_data_by_track(track_number)

    assert order_data_response.status_code == 200







