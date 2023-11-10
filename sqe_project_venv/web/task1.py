from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
import os
import os.path

driver = webdriver.Firefox()
try:
    wait = WebDriverWait(driver, 10)
    driver.get('https://www.epam.com/')

    # 1 Check the title is correct
    wait.until(EC.title_is('EPAM | Software Engineering & Product Development Services'))

    # 2 Check the ability to switch Light / Dark mode
    mode = driver.find_element(By.CSS_SELECTOR, '.header__content>.theme-switcher-ui>div.theme-switcher')
    #check mode color
    color = driver.find_element(By.CSS_SELECTOR, 'body').get_attribute("class")
    print(color)
    # switch mode
    driver.execute_script("arguments[0].click();",mode)
    # check that mode color is changed
    color_ch = driver.find_element(By.CSS_SELECTOR, 'body').get_attribute("class")
    print(color_ch)
    assert color_ch != color
    

    # 3 Check that allow to change language to UA
    # open list of language
    lang = driver.find_element(By.CSS_SELECTOR, '.location-selector__button')
    lang.click()
    # select UA
    ua = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'a.location-selector__link[href="https://careers.epam.ua"]'))).click()
    # verify that language is UA
    wait.until(EC.title_is('EPAM Ukraine - найбільша ІТ-компанія в Україні | Вакансії'))
    
    driver.find_element(By.CSS_SELECTOR, '.location-selector__button').click()
    # move back to Eng
    wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'a.location-selector__link[href="https://www.epam.com"]'))).click()
    

    # 4 Check the policies list
    # scroll to the bottom of the page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'a.fat-links[href="/investors"]')
    ))
    # check that all items are present
    driver.find_element(By.CSS_SELECTOR, 'a.fat-links[href="/services/engineering/open-source"]')
    
    driver.find_element(By.CSS_SELECTOR, 'a.fat-links[href="https://privacy.epam.com/core/interaction/showpolicy?type=CommonPrivacyPolicy"]')
    
    driver.find_element(By.CSS_SELECTOR, 'a.fat-links[href="/cookie-policy"]')
    
    driver.find_element(By.CSS_SELECTOR, 'a.fat-links[href="/applicant-privacy-notice"]')
    
    driver.find_element(By.CSS_SELECTOR, 'a.fat-links[href="/web-accessibility-statement"]')


    # 6 Check the search function
    # scroll page to the top
    driver.execute_script("window.scrollTo(0, document.body.scrollTop);")
    # click on Search
    search = driver.find_element(By.CSS_SELECTOR, '.header-search__button.header__icon')
    search.click()
    enter_data = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, '#new_form_search')
    ))
    enter_data.click()
    # type AI
    enter_data.send_keys('AI')
    driver.find_element(By.CSS_SELECTOR, '.custom-button.button-text.font-900.gradient-border-button.large-gradient-button.uppercase-text.custom-search-button').click()
    # check result
    wait.until(EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, '.search-results__counter'), 'RESULTS FOR "AI"'))
 
    
    # 7 Chack form's fields validation
    driver.get('https://www.epam.com/about/who-we-are/contact')
    #click on Submit button
    driver.find_element(By.CSS_SELECTOR, '.button-ui[type="submit"]').click()
    # check validation errors
    error_text = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "span#_content_epam_en_about_who-we-are_contact_jcr_content_content-container_section_section-par_form_constructor_user_first_name-error>span.validation-text"))).text
    assert error_text == "This is a required field"
    print(error_text)
    lastname_text = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "span#_content_epam_en_about_who-we-are_contact_jcr_content_content-container_section_section-par_form_constructor_user_last_name-error>span.validation-text"))).text
    assert lastname_text == "This is a required field"
    email_text = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "span#_content_epam_en_about_who-we-are_contact_jcr_content_content-container_section_section-par_form_constructor_user_email-error>span.validation-text"))).text
    assert email_text == "This is a required field"
    phone_text = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "span#_content_epam_en_about_who-we-are_contact_jcr_content_content-container_section_section-par_form_constructor_user_phone-error>span.validation-text"))).text
    assert phone_text == "This is a required field"
        

    # 8 Check the Company logo on the header lead to the main page
    driver.get('https://www.epam.com/about')
    # click on logo
    driver.find_element(By.CSS_SELECTOR, '.header__logo.header__logo-light').click()
    # check that url is as expected
    wait.until(EC.url_to_be('https://www.epam.com/'))


    # 9 Check that allows to download report 
    driver.get('https://www.epam.com/about')
    # scroll to Download button and click on it
    downl = driver.find_element(By.CSS_SELECTOR, 'div.colctrl__holder>div.button>div.button__wrapper.button--left>a.button-ui-23.btn-focusable>span.button__inner>span.button__content.button__content--desktop')
    driver.execute_script("arguments[0].scrollIntoView();", downl)
    downl.click()
    # check name and extension of the file
    path = 'C:/Users/Roksolana_Spryn/Downloads/EPAM_Corporate_Overview_Q3_october.pdf'
    assert os.path.isfile(path)


    # 5 Check that allow to switch location list by region
    driver.get('https://www.epam.com/')
    # scroll to Our location
    our_locat = driver.find_element(By.CSS_SELECTOR, 'span.museo-sans-light')
    driver.execute_script("arguments[0].scrollIntoView();", our_locat)
    # click on locations and check that expected countries are displayed
    driver.find_element(By.CSS_SELECTOR, 'a.tabs-23__link.js-tabs-link[data-item="2"]').click()
    wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, '.locations-viewer-23__country-btn[data-country-title="Australia"]')
    ))
    driver.find_element(By.CSS_SELECTOR, 'a.tabs-23__link.js-tabs-link[data-item="1"]')
    wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, '.locations-viewer-23__country-btn[data-country-title="Armenia"]')
    ))
    driver.find_element(By.CSS_SELECTOR, 'a.tabs-23__link.js-tabs-link[data-item="0"]')
    wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, '.locations-viewer-23__country-btn[data-country-title="Canada"]')
    ))

finally:

    driver.quit()