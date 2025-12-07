# メソッドのみなのでimportして使用してください


import time
import pyperclip
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from feature.read_env import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from getpass import getpass


def getDriver():
    chrome_options = Options()
    # ユーザーデータディレクトリとプロファイルを指定
    chrome_options.add_argument("--user-data-dir="+user_data_dir)
    chrome_options.add_argument("--profile="+profile)

    # 初めてseleniumからchromeを起動してログインする時に使用
    # ボット検知を回避するための追加オプション
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")  # WebDriverの自動化フラグを無効化
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])  # 自動化の通知を非表示

    return webdriver.Chrome(options=chrome_options)

def is_something_button(driver, search_string):
    return len(driver.find_elements(By.CSS_SELECTOR, search_string)) > 0
    
def press_something_block(driver, search_string):
    # if(WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, search_string)))):
    if(WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, search_string)))):
        print("要素が見つかりました")
        press_something_block_elements=driver.find_elements(By.CSS_SELECTOR, search_string)
        element_number=len(press_something_block_elements)-1
        # press_something_block_elements[element_number].click()
        driver.execute_script("arguments[0].click();", press_something_block_elements[element_number])
    else:
        print("要素が見つかりませんでした")
        exit(1)

def press_something_block_xpath(driver, search_string, element_number):
    # if(WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, search_string)))):
    if(WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, search_string)))):
        print("要素が見つかりました")
        press_something_block_elements=driver.find_elements(By.XPATH, search_string)
        element_number=len(press_something_block_elements)-element_number
        # press_something_block_elements[element_number].click()
        driver.execute_script("arguments[0].click();", press_something_block_elements[element_number])
    else:
        print("要素が見つかりませんでした")
        exit(1)
        
def print_elements_information(driver, search_string):
    elements = driver.find_elements(By.XPATH, search_string)

    print(f"見つかった要素の数: {len(elements)}")
    if elements:
        print("→ XPathは正しい！Seleniumでも確実に取れます")
        # 中身が見たいとき
        for i in range(0, len(elements)):
            print("element:"+str(i))
            print("tag_name:"+elements[i].tag_name)
            # print("name:"+elements[i].get_attribute("name"))
            print("class:"+elements[i].get_attribute("class"))
            print("outerHTML:"+elements[i].get_attribute("outerHTML"))
            print("innerHTML:"+elements[i].get_attribute("innerHTML"))
            print()
    else:
        print("→ 見つからない…XPathが間違ってるか、ページが変わった可能性")

def for_login(driver):
    # ログアウトしている時を考慮して、今後ログインする処理を追加する必要がある
    # 手動でログイン用
    continueString=input("処理を継続して良い場合はokと入力してください。それ以外は処理を終了します")
    if(continueString == "ok"):
        print("処理を続行します")
    else:
        print("処理を終了します")
        driver.quit()
        exit(1)
        
def for_login_getpass(driver):
    continueString=getpass("処理を継続して良い場合はokと入力してください。それ以外は処理を終了します")
    if(continueString == "ok"):
        print("処理を続行します")
    else:
        print("処理を終了します")
        driver.quit()
        exit(1)
        
def get_element(driver, search_string):
    element = driver.find_element(By.XPATH, search_string)

    return element
        
def get_elements(driver, search_string):
    elements = driver.find_elements(By.XPATH, search_string)

    return elements

def click_code_editor(driver, search_string):
    # if(WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, search_string)))):
    if(WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, search_string)))):
        print("要素が見つかりました")
        press_something_block_elements=driver.find_elements(By.CSS_SELECTOR, search_string)
            
        driver.execute_script("arguments[0].click();", press_something_block_elements[1])
        
    else:
        print("要素が見つかりませんでした")
        exit(1)
        
def get_element_by_id(driver, search_string):
    if(WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, search_string)))):
        print("要素が見つかりました")
        element=driver.find_element(By.ID, search_string)
        # print(element)
        
        return element
        
    else:
        print("要素が見つかりませんでした")
        exit(1)

def get_translated_sentence_xpath(driver, search_string):
    # if(WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, search_string)))):
    if(WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, search_string)))):
        print("検索文字列:"+search_string+"の要素が見つかりました")
        press_something_block_elements=driver.find_elements(By.XPATH, search_string)
        element_number=len(press_something_block_elements)-1
        
        return press_something_block_elements[element_number].text
    else:
        print("要素が見つかりませんでした")
        exit(1)
        
def close_code_editor(driver):
    elements = driver.find_elements(By.XPATH, '//button[@class="components-button is-next-40px-default-size is-tertiary"]')
    if(len(elements) > 0):
        driver.execute_script("arguments[0].click();", elements[0])

def open_code_editor(driver):
    press_something_block(driver, '[aria-label="オプション"]')
    press_something_block(driver, '[class="components-button components-menu-item__button components-menu-items-choice is-next-40px-default-size"]')
    click_code_editor(driver, '[class="components-button components-menu-item__button components-menu-items-choice is-next-40px-default-size"]')
    

