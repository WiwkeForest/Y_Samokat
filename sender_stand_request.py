import requests
import Configuration
def post_new_order(order_body):
    return requests.post(Configuration.URL_SERVICE + Configuration.CREATE_ORDER,
                         json=order_body,)

def get_order_data_by_track(track_number):
    return requests.get(Configuration.URL_SERVICE + Configuration.DATA_ORDER + track_number)




