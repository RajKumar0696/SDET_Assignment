import os
from selenium.webdriver.common.by import By


class FileUpload:
    btn_file_upload_id = "file-upload"
    file_path = os.path.abspath("TestData/file_upload/sample-upload-file.png")
    btn_file_submit_id = "file-submit"

    def __init__(self, driver):
        self.driver = driver

    def click_file_upload(self):
        self.driver.find_element(By.ID, self.btn_file_upload_id).send_keys(self.file_path)
        self.driver.find_element(By.ID, self.btn_file_submit_id).click()
