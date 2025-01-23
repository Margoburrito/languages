import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

language_list = {"ar", "ca", "cs", "da", "de", "en-gb", "el", "es", "fi", "fr", "it", "ko", "nl", "pl", "pt", "pt-br", "ro", "ru", "sk", "uk", "zh-hans"}


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en-gb',
                     help="Choose language")


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")

    if user_language in language_list:
        print(f"\nstart chrome browser for test, chosen language is {user_language}")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    else:
        raise pytest.UsageError("selected language is not supported")
    yield browser
    print("\nquit browser..")
    browser.quit()

