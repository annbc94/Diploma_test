# Святкина Анна selfpaced - дипломный проект, инженер по тестированию плюс.

import test_sender_stand_request
import test_data

def test_create_order_and_get_by_track():

    response_create = test_sender_stand_request.create_order(test_data.order_body)
    assert response_create.status_code == 201
    
    track = response_create.json().get("track")
    assert track is not None

    response_get = test_sender_stand_request.get_order_by_track(track)
    assert response_get.status_code == 200
    print(response_get.status_code)