import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
button_languages = dict({'ar': 'أضف الى سلة التسوق', 'ca': 'Afegeix a la cistella',
             "cs": 'Vložit do košíku', "da": 'Læg i kurv',
             'de': 'In Warenkorb legen', "en-gb": 'Add to basket',
             "el": 'Προσθήκη στο καλάθι', "es": 'Añadir al carrito',
             "fi": 'Lisää koriin', "fr": 'Ajouter au panier',
             "it": 'Aggiungi al carrello', "ko": '장바구니 담기',
             "nl": 'Voeg aan winkelmand toe', "pl": 'Dodaj do koszyka',
             "pt": 'Adicionar ao carrinho', "pt-br": 'Adicionar à cesta',
             "ro": 'Adauga in cos', "ru": 'Добавить в корзину',
             "sk": 'Pridať do košíka',"uk": 'Додати в кошик',
             "zh-hans": 'Add to basket'})
print(type(button_languages))

def test_add_button(browser):
    browser.get(link)
    button = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert button.is_displayed() is True

    chosen_language = browser.find_element(By.CSS_SELECTOR, '[selected="selected"]')
    text_button = button_languages[chosen_language.get_attribute('value')]
    assert button.text == text_button

#//*[@id="language_selector"]/div/select/option[8]
