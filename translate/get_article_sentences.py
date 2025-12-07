# python $(find . -type f -maxdepth 2 -name "get_article_sentences.py")


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

search_string = '//p[@class="block-editor-rich-text__editable block-editor-block-list__block wp-block wp-block-paragraph rich-text"]'
elements = get_elements(driver, search_string)
elements_number = len(elements)
print("要素数:"+str(elements_number))
text = ""
for element in elements:
    text = text + driver.execute_script("return arguments[0].textContent;", element).replace("\n", "") + "\n"

print(text)

with open(project_root_path+"/translate/article_sentences_folder/article_sentences"+now+".txt", "w", encoding="utf-8") as f:
    f.write(text)
        

end_time=time.time()
print("かかった時間:"+str(end_time-start_time))


driver.quit()


