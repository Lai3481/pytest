import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

@pytest.fixture
def dr_fix():
    dr = webdriver.Chrome()
    dr.maximize_window()
    dr.implicitly_wait(5)
    yield dr
    dr.close()

@pytest.fixture
def search_fix():
    return By
    
@pytest.fixture
def keys_fix():
    return Keys