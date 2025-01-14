# Скрипт проверяет цену абонементов в Территории Фитнеса г. Оренбург
from selenium import webdriver
from selenium.webdriver.common.by import By


browser = webdriver.Firefox()
browser.implicitly_wait(2)
browser.get("https://terfit.ru/cards-shop/orenburg/")

#Список с названием абонементов
price_card_name = browser.find_elements(By.CSS_SELECTOR, ".catalog-card__title")

#Список с ценами без скидки
price_card_list_promo = browser.find_elements(By.CSS_SELECTOR, ".catalog-card__price-promo")

#Список с ценами со скидкой
price_card_list = browser.find_elements(By.CSS_SELECTOR, ".catalog-card__price")

#Выводим цену всех абонементов циклом:
for i in range(len(price_card_name)):
    print(f"Актуальная цена {price_card_name[i].text}: {price_card_list[i].text}, цена без скидки {price_card_list_promo[i].text}")

browser.quit()