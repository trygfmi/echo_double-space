# python $(find . -type f -maxdepth 2 -name "get_article_headings.py")


import time
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from feature.use_selenium_feature import getDriver, get_elements, close_code_editor
from feature.read_env import *
from datetime import datetime
import subprocess


project_root_path = subprocess.run(f'echo "$(dirname "$(dirname "$(readlink -f "{__file__}")")")"', shell=True, capture_output=True, text=True).stdout.strip()
start_time=time.time()

now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
driver = getDriver()
driver.get(access_url)
title = driver.title
print(title)

close_code_editor(driver)

search_h2_string = '//h2[@class="block-editor-rich-text__editable block-editor-block-list__block wp-block wp-block-heading rich-text"]'
elements = get_elements(driver, search_h2_string)
elements_number = len(elements)
print("要素数:"+str(elements_number))
text = ""
for element in elements:
    text = text + driver.execute_script("return arguments[0].textContent;", element).replace("\n", "") + "\n"

print(text)

with open(project_root_path+"/translate/article_headings_folder/article_headings"+now+".txt", "w", encoding="utf-8") as f:
    f.write(text)
    

time.sleep(1)
now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
search_h3_string = '//h3[@class="block-editor-rich-text__editable block-editor-block-list__block wp-block wp-block-heading rich-text"]'
elements = get_elements(driver, search_h3_string)
elements_number = len(elements)
print("要素数:"+str(elements_number))
text = ""
for element in elements:
    text = text + driver.execute_script("return arguments[0].textContent;", element).replace("\n", "") + "\n"

print(text)

with open(project_root_path+"/translate/article_headings_folder/article_headings"+now+".txt", "w", encoding="utf-8") as f:
    f.write(text)
    

time.sleep(1)
now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
search_h4_string = '//h4[@class="block-editor-rich-text__editable block-editor-block-list__block wp-block wp-block-heading rich-text"]'
elements = get_elements(driver, search_h4_string)
elements_number = len(elements)
print("要素数:"+str(elements_number))
text = ""
for element in elements:
    text = text + driver.execute_script("return arguments[0].textContent;", element).replace("\n", "") + "\n"

print(text)

with open(project_root_path+"/translate/article_headings_folder/article_headings"+now+".txt", "w", encoding="utf-8") as f:
    f.write(text)
    

time.sleep(1)
now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
search_h5_string = '//h5[@class="block-editor-rich-text__editable block-editor-block-list__block wp-block wp-block-heading rich-text"]'
elements = get_elements(driver, search_h5_string)
elements_number = len(elements)
print("要素数:"+str(elements_number))
text = ""
for element in elements:
    text = text + driver.execute_script("return arguments[0].textContent;", element).replace("\n", "") + "\n"

print(text)

with open(project_root_path+"/translate/article_headings_folder/article_headings"+now+".txt", "w", encoding="utf-8") as f:
    f.write(text)
        

end_time=time.time()
print("かかった時間:"+str(end_time-start_time))


driver.quit()


