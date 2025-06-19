import requests
import test_configuration
import test_data

def create_order(order_body):
    return requests.post(test_configuration.URL_SERVICE + test_configuration.CREATE_ORDER_PATH, json=order_body)

def get_order_by_track(track):
    return requests.get(test_configuration.URL_SERVICE + test_configuration.GET_ORDER_BY_TRACK_PATH, params={"t": track})

