# Скрипт проверяет цену абонемента "Спортивное утро" в Территории Фитнеса г. Оренбург
from selenium import webdriver
from selenium.webdriver.common.by import By


browser = webdriver.Firefox()
browser.implicitly_wait(10)
browser.get("https://terfit.ru/cards-shop/orenburg/")

#Тут лежат все названия
price_card_name = browser.find_elements(By.CSS_SELECTOR, ".catalog-card__title")

#Тут лежат все цены
price_card_list = browser.find_elements(By.CSS_SELECTOR, ".catalog-card__price")

#Выводим цену всех абонементов циклом:
for i in range(len(price_card_name)):
    print(f"Цена {price_card_name[i].text}: {price_card_list[i].text}")

browser.quit()