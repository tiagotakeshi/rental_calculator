#!/usr/bin/env python
# coding: utf-8

# In[1]:


# libraries
from selenium import webdriver
from time import sleep
import pandas as pd
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime


# In[2]:


# links 
url = 'https://www.vivareal.com.br/aluguel/sp/sao-jose-dos-campos/apartamento_residencial/'


# In[3]:


driver = webdriver.Chrome()
driver.get(url)
sleep(4)
actions = ActionChains(driver)


# In[4]:


listas = []
url_check = ['']


# In[5]:


try:
    driver.find_element_by_class_name("cookie-notifier__cta").click()
except:
    print("No cookies!")

while True:
    try:
        driver.find_element_by_class_name("cookie-notifier__cta").click()
    except:
        pass
    sleep(10)
    result = driver.find_element_by_xpath('//*[@id="js-site-main"]/div[2]/div[1]/section/div[2]')
    list_apto = result.find_elements_by_class_name("js-property-card")
    for i,apto in enumerate(list_apto):
        link = apto.find_element_by_class_name("js-card-title").get_attribute('href')
        if link not in url_check:
            id_apto = link.split("id-")[-1][:-1]
            adress = apto.find_element_by_class_name("property-card__address").text
            area = apto.find_element_by_class_name("js-property-card-detail-area").text
            bedrooms = apto.find_element_by_class_name("js-property-detail-rooms").text
            bathrooms = apto.find_element_by_class_name("js-property-detail-bathroom").text
            garage = apto.find_element_by_class_name("js-property-detail-garages").text
            price = apto.find_element_by_class_name("js-property-card-prices").text
            try:
                others = apto.find_element_by_class_name("property-card__amenities").text
            except:
                others = None
            try:
                cond = apto.find_element_by_class_name("js-condo-price").text
            except:
                cond = None
            listas.append({"id": id_apto,
                           "link": link,
                           "address": adress,
                           "area": area,
                           "bedrooms": bedrooms,
                           "bathrooms": bathrooms,
                           "garages": garage,
                           "others": others,
                           "price": price,
                           "condo": cond,
                           "date": datetime.now().strftime("%Y-%m-%d %H:%M")})
            url_check.append(link)
        else:
            pass
    paginator = driver.find_element_by_class_name("js-results-pagination")
    next_page = paginator.find_element_by_xpath("//a[@title='Próxima página']")
    try:
        next_page.click()
    except:
        break

df = pd.DataFrame(listas).to_csv("apto_results.csv", index=False)
driver.close()


# In[ ]:




