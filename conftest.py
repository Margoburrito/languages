import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as firefoxOptions
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile

language_list = {"ar", "ca", "cs", "da", "de", "en-gb", "el", "es", "fi", "fr", "it", "ko", "nl", "pl", "pt", "pt-br", "ro", "ru", "sk", "uk", "zh-hans"}


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en-gb',
                     help="Choose language")
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        if user_language in language_list:
            print(f"\nchosen language is {user_language}")
            options = Options()
            options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
            browser = webdriver.Chrome(options=options)
        else:
            raise pytest.UsageError("selected language is not supported")
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        if user_language in language_list:
            print(f"\nchosen language is {user_language}")
            options = firefoxOptions()
            firefox_profile = FirefoxProfile()
            firefox_profile.set_preference("intl.accept_languages", user_language)
            options.profile = firefox_profile
            browser = webdriver.Firefox(options=options)
        else:
            raise pytest.UsageError("selected language is not supported")

    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    yield browser
    print("\nquit browser..")
    browser.quit()

