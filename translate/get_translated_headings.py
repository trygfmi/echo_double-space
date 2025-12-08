# python $(find . -type f -maxdepth 2 -name "get_translated_headings.py")


import time
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from feature.use_selenium_feature import getDriver, get_translated_sentence_xpath
from feature.read_env import *
import subprocess
from datetime import datetime


project_root_path = subprocess.run(f'echo "$(dirname "$(dirname "$(readlink -f "{__file__}")")")"', shell=True, capture_output=True, text=True).stdout.strip()

start_time=time.time()

driver = getDriver()
driver.get(access_url)
title = driver.title
print(title)

now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
translated_sentences = ""
search_string = '//div[@class="QcsUad BDJ8fb sMVRZe hCXDsb wneUed"]//div[@class="lRu31"]'
latest_article_sentences = subprocess.run(f"ls -1t {project_root_path}/translate/article_headings_folder | sed -n '4p'", shell=True, capture_output=True, text=True).stdout.strip()
with open(project_root_path+"/translate/article_headings_folder/"+latest_article_sentences, "r", encoding="utf-8") as sentences:
    for i, sentence in enumerate(sentences):
        print(str(i)+":"+sentence)
        
        driver.execute_script("""
                              let sentence = arguments[0];
                              let url = "https://translate.google.com/?sl=ja&tl=en&text=" + sentence + "&op=translate"
                              window.location.href = url
                              """
                              , sentence)

        translated_text = get_translated_sentence_xpath(driver, search_string)
        translated_sentences = translated_sentences + translated_text.replace("\n", "") + "\n"

with open(project_root_path+"/translate/translated_headings_folder/translated_headings"+now+".txt", "w", encoding="utf-8") as f:
    f.write(translated_sentences)


now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
translated_sentences = ""
search_string = '//div[@class="QcsUad BDJ8fb sMVRZe hCXDsb wneUed"]//div[@class="lRu31"]'
latest_article_sentences = subprocess.run(f"ls -1t {project_root_path}/translate/article_headings_folder | sed -n '3p'", shell=True, capture_output=True, text=True).stdout.strip()
with open(project_root_path+"/translate/article_headings_folder/"+latest_article_sentences, "r", encoding="utf-8") as sentences:
    for i, sentence in enumerate(sentences):
        print(str(i)+":"+sentence)
        
        driver.execute_script("""
                              let sentence = arguments[0];
                              let url = "https://translate.google.com/?sl=ja&tl=en&text=" + sentence + "&op=translate"
                              window.location.href = url
                              """
                              , sentence)

        translated_text = get_translated_sentence_xpath(driver, search_string)
        translated_sentences = translated_sentences + translated_text.replace("\n", "") + "\n"

with open(project_root_path+"/translate/translated_headings_folder/translated_headings"+now+".txt", "w", encoding="utf-8") as f:
    f.write(translated_sentences)
    
    
now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
translated_sentences = ""
search_string = '//div[@class="QcsUad BDJ8fb sMVRZe hCXDsb wneUed"]//div[@class="lRu31"]'
latest_article_sentences = subprocess.run(f"ls -1t {project_root_path}/translate/article_headings_folder | sed -n '2p'", shell=True, capture_output=True, text=True).stdout.strip()
with open(project_root_path+"/translate/article_headings_folder/"+latest_article_sentences, "r", encoding="utf-8") as sentences:
    for i, sentence in enumerate(sentences):
        print(str(i)+":"+sentence)
        
        driver.execute_script("""
                              let sentence = arguments[0];
                              let url = "https://translate.google.com/?sl=ja&tl=en&text=" + sentence + "&op=translate"
                              window.location.href = url
                              """
                              , sentence)

        translated_text = get_translated_sentence_xpath(driver, search_string)
        translated_sentences = translated_sentences + translated_text.replace("\n", "") + "\n"

with open(project_root_path+"/translate/translated_headings_folder/translated_headings"+now+".txt", "w", encoding="utf-8") as f:
    f.write(translated_sentences)
    
    
now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
translated_sentences = ""
search_string = '//div[@class="QcsUad BDJ8fb sMVRZe hCXDsb wneUed"]//div[@class="lRu31"]'
latest_article_sentences = subprocess.run(f"ls -1t {project_root_path}/translate/article_headings_folder | sed -n '1p'", shell=True, capture_output=True, text=True).stdout.strip()
with open(project_root_path+"/translate/article_headings_folder/"+latest_article_sentences, "r", encoding="utf-8") as sentences:
    for i, sentence in enumerate(sentences):
        print(str(i)+":"+sentence)
        
        driver.execute_script("""
                              let sentence = arguments[0];
                              let url = "https://translate.google.com/?sl=ja&tl=en&text=" + sentence + "&op=translate"
                              window.location.href = url
                              """
                              , sentence)

        translated_text = get_translated_sentence_xpath(driver, search_string)
        translated_sentences = translated_sentences + translated_text.replace("\n", "") + "\n"

with open(project_root_path+"/translate/translated_headings_folder/translated_headings"+now+".txt", "w", encoding="utf-8") as f:
    f.write(translated_sentences)

    
    
end_time=time.time()
print("かかった時間:"+str(end_time-start_time))


driver.quit()
