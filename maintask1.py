from selenium import webdriver
import datetime
import time
import os

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
DRIVER_BIN = os.path.join(PROJECT_ROOT, "chromedriver")

options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(options=options, executable_path = DRIVER_BIN)

driver.get("https://www.udemy.com/course/flutter-dart-the-complete-flutter-app-development-course/")

driver.set_page_load_timeout(30)

button = driver.find_element_by_class_name("section-container--more-sections")
button.click()

elements = driver.find_elements_by_css_selector("div.lecture-container.lecture-container--preview")
new_lst = []
for i in elements:
    new_lst.append([i.find_element_by_class_name("title").find_element_by_tag_name("a").get_property("innerText"), 
                    i.find_element_by_class_name("content-summary").get_property("innerText")])

new_lst.sort(key=lambda x: datetime.time.fromisoformat(x[1]))

for i in new_lst:
    print(i[0] + "  " + i[1])

driver.close()