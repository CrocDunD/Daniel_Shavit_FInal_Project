import allure

from utilities.common_ops import get_data
from extensions.verifications import Verifications as ver
from workflows.api_flows import Api_Flows as flow

domain = get_data("Api_Url")

class Test_App_Adidas:


    allure.title('Add comment')
    allure.step('Test adding new comment using API')
    def test_add_new_comment(self):
        payload = {
    "userId": 11,
    "title": "huh?",
    "body": "what?"
  }
        response = flow.new_post(payload, None, None)
        print("status code is " + str(response.status_code))


    allure.title('Test false ToDo percentage')
    allure.step('Test if the amount of todos that are finished is bigger than the specified amount')
    def test_done_todos(self):
        upper_bound_completed = float(get_data("completed_percentage_upper_bound"))
        all_count = len(flow.get_all_todos(None,None).json())
        completed_count = len(flow.get_completed_todos(None,None).json())
        print("all: " + str(all_count) + "and completed: " + str(completed_count))
        completed_percentage = completed_count/all_count
        ver.verify_bigger_number(completed_percentage,upper_bound_completed)


    allure.title('Test updating a completed todo')
    allure.step('Test updating a todo from false to true with a specified ID')
    def test_update_todo(self):
        id = get_data("todo_id_to_update")
        payload ={
            "completed" : True
        }
        flow.update_todo(id, payload, None, None)








#update to do from false to true
# #get the number of photos in a specified album

#open geo loaction of a specified user