from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Firefox()
try:
    wait = WebDriverWait(driver, 30)

    driver.get('https://demowebshop.tricentis.com/')

    # 1 allows register a User
    # click register
    wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'a.ico-register')
    )).click() 
    # check radio button                                   
    wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'input#gender-female')
    )).click()     
    # fill in all info                               
    first_name = driver.find_element(By.CSS_SELECTOR, 'input#FirstName') 
    first_name.send_keys('Roksolana')

    last_name = driver.find_element(By.CSS_SELECTOR, 'input#LastName')
    last_name.send_keys('Name')

    email = driver.find_element(By.CSS_SELECTOR, 'input#Email')
    email.send_keys('RoksolanaName22@gmail.com')

    password = driver.find_element(By.CSS_SELECTOR, 'input#Password')
    password.send_keys('Newpassword123')

    conf_password = driver.find_element(By.CSS_SELECTOR, 'input#ConfirmPassword')
    conf_password.send_keys('Newpassword123')
    # click register button
    driver.find_element(By.CSS_SELECTOR, 'input#register-button').click()  

    message = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'div.result')
    ))

    assert 'Your registration completed' in message.text
    # logout
    driver.find_element(By.CSS_SELECTOR, 'a.ico-logout').click()  


    # 2 allows login a User
     # click login
    wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'a.ico-login')
    )).click()                                    
    #fill in email
    enter_email = wait.until(EC.presence_of_element_located(   
        (By.CSS_SELECTOR, 'input#Email')
    ))
    enter_email.send_keys('RoksolanaName11@gmail.com') 

    enter_password = driver.find_element(By.CSS_SELECTOR, 'input#Password')
    enter_password.send_keys('Newpassword123')
    # click on login button
    driver.find_element(By.CSS_SELECTOR, 'input.button-1.login-button').click() 


    # 3 	Verify that ‘Computers’ group has 3 sub-groups with correct names
    # go to Computers
    wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'a[href="/computers"]')
    )).click()                                       
    # check 3 subtabs
    wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'a[href="/accessories"]')   
    ))
    driver.find_element(By.CSS_SELECTOR, 'a[href="/notebooks"]')
    driver.find_element(By.CSS_SELECTOR, 'a[href="/desktops"]>img').click()


    # 4 allows sorting items 
    sort = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'select#products-orderby')
    ))
    sort.click()
    # check all items in Sort by drop down list one by one
    wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, '#products-orderby > option:nth-child(2)')
    )).click()  

    wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'select#products-orderby')
    )).click()
    wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, '#products-orderby > option:nth-child(3)')
    )).click()

    wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'select#products-orderby')
    )).click()
    wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, '#products-orderby > option:nth-child(4)')
    )).click()

    wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'select#products-orderby')
    )).click()
    wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, '#products-orderby > option:nth-child(5)')
    )).click()

    wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'select#products-orderby')
    )).click()
    wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, '#products-orderby > option:nth-child(6)')
    )).click()

    wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'select#products-orderby')
    )).click()
    wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, '#products-orderby > option:nth-child(1)')
    )).click()


    # 5 allows changing number of items on page
    driver.find_element(By.CSS_SELECTOR, 'select#products-pagesize').click()
    # check all Display items per page one by one
    wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, '#products-pagesize > option:nth-child(1)')
    )).click()

    driver.find_element(By.CSS_SELECTOR, 'select#products-pagesize').click()
    wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, '#products-pagesize > option:nth-child(3)')
    )).click()

    driver.find_element(By.CSS_SELECTOR, 'select#products-pagesize').click()
    wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, '#products-pagesize > option:nth-child(2)')
    )).click()


    # 6 allows adding an item to the Wishlist
    # go to an element
    wait.until(EC.presence_of_element_located(           
        (By.CSS_SELECTOR, 'a[href="/electronics"]')
    )).click()
    wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'a[href="/cell-phones"]>img')
    )).click()
    wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'a[href="/smartphone"]')
    )).click()
    # add to wish list
    wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'input#add-to-wishlist-button-43') 
    )).click()
    # check that wish list is not empty
    wishlist_item = driver.find_element(By.CSS_SELECTOR, 'span.wishlist-qty') 
    assert wishlist_item != 0


    # 7 allows adding an item to the card
    # add element to cart
    driver.find_element(By.CSS_SELECTOR, 'input#add-to-cart-button-43').click() 
    # check that cart is not empty
    cart_item = driver.find_element(By.CSS_SELECTOR, 'span.cart-qty') 
    assert cart_item != 0


    # 8 allows removing an item from the card
    # open Shopping cart
    driver.find_element(By.CSS_SELECTOR, 'span.cart-label').click() 
    # check remove checkbox
    check = wait.until(EC.presence_of_element_located(     
        (By.CSS_SELECTOR, 'input[type="checkbox"]')
    )).click()
    # click on Update shopping cart
    driver.find_element(By.CSS_SELECTOR, 'input.button-2.update-cart-button').click() 
    # verify that shopping cart is not empty
    card_message = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'div.order-summary-content')
    ))
    assert "Your Shopping Cart is empty!" in card_message.text


    # 9 allows checkout an item 
    wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'a[href="/electronics"]')
    )).click()
    wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'a[href="/cell-phones"]>img')
    )).click()
    wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'a[href="/phone-cover"]')
    )).click()
    #added item to cart
    wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'input#add-to-cart-button-80.button-1.add-to-cart-button') 
    )).click()
    #go to Shopping cart
    driver.find_element(By.CSS_SELECTOR, 'span.cart-label').click() 
    #check check box
    wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'input#termsofservice') 
    )).click()
    #click checkout
    driver.find_element(By.CSS_SELECTOR, 'button#checkout').click() 
    #go through all information to complete checkout
    wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'input.button-1.new-address-next-step-button') 
    )).click()
    sa = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'input.button-1.new-address-next-step-button[onclick="Shipping.save()"]')
    ))
    driver.execute_script("arguments[0].scrollIntoView();", sa)
    wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'input#PickUpInStore')
    )).click()
    driver.find_element(By.CSS_SELECTOR, 'input.button-1.new-address-next-step-button[onclick="Shipping.save()"]').click()
    
    wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'input.button-1.payment-method-next-step-button')
    )).click()
    wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'input.button-1.payment-info-next-step-button')
    )).click()
    wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'input.button-1.confirm-order-next-step-button')
    )).click()



finally:

    driver.quit()
    

