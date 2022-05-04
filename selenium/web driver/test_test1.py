# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestTest():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_test(self):
    self.driver.get("http://localhost:8080/LMS/")
    self.driver.set_window_size(790, 438)
    self.driver.find_element(By.NAME, "user_name").send_keys("j")
    self.driver.find_element(By.NAME, "password").click()
    self.driver.find_element(By.NAME, "password").send_keys("j")
    self.driver.find_element(By.NAME, "signin").click()
    self.driver.find_element(By.LINK_TEXT, "Student").click()
    self.driver.find_element(By.ID, "search").click()
    self.driver.find_element(By.LINK_TEXT, "Add Student").click()
    self.driver.find_element(By.NAME, "admission_no").click()
    self.driver.find_element(By.NAME, "admission_no").send_keys("123")
    self.driver.find_element(By.NAME, "student_name").click()
    self.driver.find_element(By.NAME, "student_name").send_keys("prasad")
    self.driver.find_element(By.NAME, "grade").click()
    self.driver.find_element(By.NAME, "grade").send_keys("10")
    self.driver.find_element(By.NAME, "section").click()
    self.driver.find_element(By.NAME, "section").send_keys("A")
    self.driver.find_element(By.NAME, "profile").click()
    self.driver.find_element(By.NAME, "profile").send_keys("asd")
    self.driver.find_element(By.CSS_SELECTOR, ".btn-default").click()
  
