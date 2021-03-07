import time
def loginFun(driver):
    print("Enter the number corresponding to your preferred login method.")
    print("1. Facebook")
    print("2. Google")
    print("3. Phone number")
    print("4. Username and Password\n")
    loginMethod=0
    while(True):
        loginMethod = input().strip()
        if loginMethod in ['1','2','3','4']:
            loginMethod=int(loginMethod)
            break
        else:
            print("Not a valid entry.")
    driver.get("https://open.spotify.com/")
    time.sleep(5)
    loginbutton = driver.find_element_by_css_selector('[data-testid="login-button"]')
    loginbutton.click()
    time.sleep(5)
    loginLinks = driver.find_elements_by_class_name('btn')
    if loginMethod == 1:
        facebook = loginLinks[0]
        facebook.click()
        facebookUsername = input("Enter Facebook Username: ")
        facebookPassword = input("Enter Facebook Password: ")
        username = driver.find_element_by_id("email")
        username.send_keys(facebookUsername)
        passw = driver.find_element_by_id("pass")
        passw.send_keys(facebookPassword)
        login = driver.find_element_by_id("loginbutton")
        login.click()
    elif loginMethod == 2:
        directlogin = loginLinks[4]
        directlogin.click()
        Username = input("Enter Email ID: ").strip()
        Password = input("Enter Password: ").strip()
        username = driver.find_element_by_id("login-username")
        username.send_keys(Username)
        passw = driver.find_element_by_id("login-password")
        passw.send_keys(Password)
        button=driver.find_element_by_id("login-button")
        button.click()
    elif loginMethod == 3:
        phoneNumber = loginLinks[3]
        phoneNumber.click()
        phonenum=input("Enter your phone number: ").strip()
        p=driver.find_element_by_id("phonelogin-phonenumber")
        p.send_keys(phonenum)
        enterbutton=driver.find_element_by_id("phonelogin-button")
        enterbutton.click()
        otp=input("Enter the 6 digit OTP sent to your phone number: ").strip()
        q=driver.find_element_by_id("phonelogin-code")
        q.send_keys(otp)
        button=driver.find_element_by_id("code-button")
        button.click()
    elif loginMethod == 4:
        directlogin = loginLinks[4]
        directlogin.click()
        Username = input("Enter Username/Email: ").strip()
        Password = input("Enter Password: ").strip()
        username = driver.find_element_by_id("login-username")
        username.send_keys(Username)
        passw = driver.find_element_by_id("login-password")
        passw.send_keys(Password)
        button=driver.find_element_by_id("login-button")
        button.click()