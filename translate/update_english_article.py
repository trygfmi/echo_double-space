# python $(find . -type f -maxdepth 2 -name "update_english_article.py")


import time
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from feature.use_selenium_feature import getDriver, get_elements, press_something_block_xpath
from feature.read_env import *
import subprocess


project_root_path = subprocess.run(f'echo "$(dirname "$(dirname "$(readlink -f "{__file__}")")")"', shell=True, capture_output=True, text=True).stdout.strip()

start_time=time.time()

driver = getDriver()
driver.get(english_article_url)
title = driver.title
print(title)

search_string = '//p[@class="block-editor-rich-text__editable block-editor-block-list__block wp-block wp-block-paragraph rich-text"]'
elements = get_elements(driver, search_string)
elements_number = len(elements)
print("要素数:"+str(elements_number))

latest_translated_sentences=subprocess.run(f"ls -1t {project_root_path}/translate/translated_sentences_folder | sed -n '1p'", shell=True, capture_output=True, text=True).stdout.strip()
with open(project_root_path+"/translate/translated_sentences_folder/"+latest_translated_sentences, "r", encoding="utf-8") as f:
    for element, line in zip(elements, f):
        driver.execute_script("""
                            let new_text = arguments[1];
                            arguments[0].textContent = new_text;
                            """
                            , element, line)

for i, element in enumerate(elements):
    text = driver.execute_script("return arguments[0].textContent;", element).replace("\n", "")
    print(str(i)+":"+text)

search_save_button_string='//button[@class="components-button editor-post-publish-button editor-post-publish-button__button is-primary is-compact"]'
element_number=1
press_something_block_xpath(driver, search_save_button_string, element_number)
 
time.sleep(5)
end_time=time.time()
print("かかった時間:"+str(end_time-start_time))


driver.quit()
