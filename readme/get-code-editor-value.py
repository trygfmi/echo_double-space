# python get-code-editor-value.py
# python $(find . -type f -maxdepth 2 -name "get-code-editor-value.py")


import time
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from feature.use_selenium_feature import  getDriver, open_code_editor, get_element_by_id
from feature.read_env import *
import subprocess


project_root_path = subprocess.run(f'echo "$(dirname "$(dirname "$(readlink -f "{__file__}")")")"', shell=True, capture_output=True, text=True).stdout.strip()

start_time=time.time()

driver = getDriver()
driver.get(access_url)
title = driver.title
print(title)

open_code_editor(driver)

input_element = get_element_by_id(driver, "post-content-0")

code_editor_string = input_element.get_attribute("value")
with open(project_root_path+"/README.md", "w", encoding="utf-8") as f:
    f.write(code_editor_string)

end_time=time.time()
print("かかった時間:"+str(end_time-start_time))

driver.quit()


