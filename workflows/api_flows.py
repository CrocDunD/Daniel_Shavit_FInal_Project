import allure

from utilities.common_ops import get_data
from extensions.api_actions import Api_Actions as api_a


url = get_data('Api_Url')

class Api_Flows:

    @staticmethod
    @allure.step('New post')
    def new_post(payload, user, password):
        return api_a.post(url + "posts", payload, user, password)

    @staticmethod
    @allure.step('Get all todos')
    def get_all_todos(user, password):
        return api_a.get(url + "todos" ,None,None)


    @staticmethod
    @allure.step('Get completed todos')
    def get_completed_todos(user, password):
        return api_a.get(url + "todos?completed=true" ,None,None)


    @staticmethod
    @allure.step('update todo')
    def update_todo(id, payload, user, password):
        current_status = api_a.get(url + "todos/" + id,None,None).json()["completed"]
        assert current_status != True, "This Todo is already completed"
        return api_a.put(url + "todos/" + id, payload, user, password)