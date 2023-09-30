import csv
import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from test_cases import conftest
import xml.etree.ElementTree as ET


def get_data(node_name):
    root = ET.parse('C:/Users/daniels/PycharmProjects/Final_Automation Project_Daniel_Shavit/configuration/data.xml').getroot()
    return root.find(".//" + node_name).text

def read_csv(file_name):
    data = []
    with open(file_name, newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            data.insert(len(data),row)
        return data


def wait(for_element, elem):
    if for_element == 'element exists':
        WebDriverWait(conftest.driver, 5).until(EC.presence_of_element_located((elem[0], elem[1])))
    elif for_element == 'element displayed':
        WebDriverWait(conftest.driver, 5).until(EC.visibility_of_element_located((elem[0], elem[1])))

#Enum for selecting displayed elements or existing elelemnts
class For:
    ELEMENT_EXISTS = 'element exists'
    ELEMENT_DISPLAYED = 'element displayed'

class By:
    USER = 'user'
    INDEX = 'index'


def get_timestamp():
    return time.time()