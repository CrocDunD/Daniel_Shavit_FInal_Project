import allure

from utilities.common_ops import get_data
from extensions.api_actions import Api_Actions as api_a


url = get_data('Api_Url')

class Api_Flows:

    @staticmethod
    @allure.step('New post')
    def new_post(payload, user, password):
        response = api_a.post(url + "posts", payload, user, password)
        return response

    @staticmethod
    @allure.step('Get all todos')
    def get_all_todos(user, password):
        response = api_a.get(url + "todos" ,None,None)
        return response


    @staticmethod
    @allure.step('Get completed todos')
    def get_completed_todos(user, password):
        response = api_a.get(url + "todos?completed=true" ,None,None)
        return response


    @staticmethod
    @allure.step('update todo')
    def update_todo(id, payload, user, password):
        current_status = api_a.get(url + "todos/" + id,None,None).json()["completed"]
        assert current_status != True, "This Todo is already completed"
        return api_a.put(url + "todos/" + id, payload, user, password)


    @staticmethod
    @allure.step('get album by name')
    def get_album_by_name(name, user, password):
        response = api_a.get(url + 'albums?title=' + name, user, password)
        assert len(response.json()) > 0, 'Specified album not found'
        return response

    @staticmethod
    @allure.step('get photos by album id')
    def get_photos_by_album_id(id, user, password):
        response = api_a.get(url + 'photos?albumId=' + id, user, password)
        return response


    @staticmethod
    @allure.step('get user geo location')
    def get_user_geoloc(id, user, password):
        user = api_a.get(url + 'users?id=' + id, user, password)
        lat = api_a.extract_value_from_response(user, [0,'address','geo','lat'])
        lng = api_a.extract_value_from_response(user, [0,'address','geo','lng'])
        return [lat,lng]
