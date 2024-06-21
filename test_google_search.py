import pytest
from selene import browser, have


def test_google_search_positive():
    browser.open('')
    browser.element('[name=q]').type('Capital of Uruguay').press_enter()
    browser.element('[class=xpdopen]').should(have.text('Montevideo. '))


def test_google_search_negative():
    browser.open('')
    text = 'dfstetgtgtgtgtgtgtvb2363kikikik'
    browser.element('[name=q]').type(text).press_enter()
    browser.element('[class=kp-header]').should(have.text(f'По запросу {text} ничего не найдено. '))

