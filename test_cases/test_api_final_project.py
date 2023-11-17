import time

import allure
import pytest
from selenium.webdriver.common.by import By

from test_cases import conftest
from utilities.common_ops import get_data
from extensions.verifications import Verifications as ver
from workflows.api_flows import Api_Flows as flow

domain = get_data("Api_Url")
user = get_data("UserName")
password = get_data("Password")

class Test_App_Adidas:


    allure.title('Add comment')
    allure.description('Test adding new comment using API')
    def test_add_new_comment(self):
        payload = {
    "userId": 11,
    "title": "huh?",
    "body": "what?"
  }
        response = flow.new_post(payload, user, password)
        print("status code is " + str(response.status_code))


    allure.title('Test false ToDo percentage')
    allure.description('Test if the amount of todos that are finished is bigger than the specified amount')
    def test_done_todos(self):
        upper_bound_completed = float(get_data("completed_percentage_upper_bound"))
        all_count = len(flow.get_all_todos(user, password).json())
        completed_count = len(flow.get_completed_todos(user, password).json())
        print("all: " + str(all_count) + "and completed: " + str(completed_count))
        completed_percentage = completed_count/all_count
        ver.verify_bigger_number(completed_percentage,upper_bound_completed)


    allure.title('Test updating a completed todo')
    allure.description('Test updating a todo from false to true with a specified ID')
    def test_update_todo(self):
        id = get_data("todo_id_to_update")
        payload ={
            "completed" : True
        }
        response = flow.update_todo(id, payload, user, password)
        ver.verify_equals(response.status_code,200)


    allure.title('Test album photo count')
    allure.description('Test getting photos count of a specified album')
    def test_photo_count(self):
        album_title = get_data("Album_Name")
        album = flow.get_album_by_name(album_title, user, password)
        album_id = str(album.json()[0]["id"])
        photos = flow.get_photos_by_album_id(album_id, user, password)
        photos_count = len(photos.json())
        print('Number of photos is selected album: ' + str(photos_count))


    allure.title('Test open user location')
    allure.description('Test getting and opening user location on a browser')
    @pytest.mark.usefixtures('init_web_driver_adidas')
    def test_open_user_location(self):
        user_id = get_data("User_Id")
        geo_loc = flow.get_user_geoloc(user_id,user,password)
        conftest.driver.get('https://www.google.com/maps')
        search_box = conftest.driver.find_element(By.XPATH, '//*[@id="searchboxinput"]')
        search_box.send_keys(geo_loc[0] + ' ' + geo_loc[1])
        conftest.driver.find_element(By.XPATH, '//*[@id="searchbox-searchbutton"]').click()
        time.sleep(5)
        print(conftest.driver.current_url)
