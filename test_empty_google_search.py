from selene import browser
from selene import be, have




def test_google(settings):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('kjvhgcfhxjgc,nchtxm').press_enter()
    browser.element('[id="result-stats"]').should(have.text('Результатов: примерно 0'))