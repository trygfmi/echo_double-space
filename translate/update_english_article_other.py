# python $(find . -type f -maxdepth 2 -name "update_english_article_other.py")


import time
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from feature.use_selenium_feature import getDriver, get_elements, press_something_block_xpath
from feature.read_env import *
import subprocess
from selenium.webdriver.common.by import By


project_root_path = subprocess.run(f'echo "$(dirname "$(dirname "$(readlink -f "{__file__}")")")"', shell=True, capture_output=True, text=True).stdout.strip()

start_time=time.time()

driver = getDriver()
driver.get(english_article_url)
title = driver.title
print(title)

search_list_string = '//div[@aria-label="リストのテキスト"]'
elements = get_elements(driver, search_list_string)
elements_number = len(elements)
print("要素数:"+str(elements_number))

for element in elements:
    driver.execute_script("""
                        arguments[0].textContent = "None in paticular";
                        """
                        , element)

search_output_string = '//div[text()="出力結果"]'
elements = get_elements(driver, search_output_string)
elements_number = len(elements)
print("要素数:"+str(elements_number))

for element in elements:
    driver.execute_script("""
                        arguments[0].textContent = "Output"
                        """
                        , element)

search_open_detail_string = '//div[text()="クリックして詳細を開く"]'
elements = get_elements(driver, search_open_detail_string)
elements_number = len(elements)
print("要素数:"+str(elements_number))

for element in elements:
    driver.execute_script("""
                        arguments[0].textContent = "Click to open details"
                        """
                        , element)
    
search_detail_string = '//div[text()="詳細"]'
elements = get_elements(driver, search_detail_string)
elements_number = len(elements)
print("要素数:"+str(elements_number))

for element in elements:
    driver.execute_script("""
                        arguments[0].textContent = "Detail";
                        """
                        , element)
    
search_no_code_string = '//*[text()="特にありません"]'
# search_no_code_string = '//*[@class="block-editor-block-list__block wp-block"]'
elements = get_elements(driver, search_no_code_string)
elements_number = len(elements)
print("要素数:"+str(elements_number))

for element in elements:
    driver.execute_script("""
                        const blockElement = arguments[0];

                        const clientId = blockElement.getAttribute('data-block');
                        wp.data.dispatch('core/block-editor').updateBlockAttributes(clientId, { content: "Nothing in paticular" })
                        """
                        , element.find_element(By.XPATH, "../../.."))


driver.execute_script("""
    // 全要素にinputイベントを発火（Reactが変更を認識）
    document.querySelectorAll('[contenteditable="true"]').forEach(el => {
        const inputEvent = new Event('input', { bubbles: true, cancelable: true });
        inputEvent.inputType = 'insertText';
        el.dispatchEvent(inputEvent);
    });
""")

input()

search_save_button_string='//button[@class="components-button editor-post-publish-button editor-post-publish-button__button is-primary is-compact"]'
element_number=1
press_something_block_xpath(driver, search_save_button_string, element_number)
 
time.sleep(5)
end_time=time.time()
print("かかった時間:"+str(end_time-start_time))


driver.quit()
