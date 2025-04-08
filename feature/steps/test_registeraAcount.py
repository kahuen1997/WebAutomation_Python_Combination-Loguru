import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.options import Options
from loguru import *

@given(u'User opens the browser')
def step_impl(context):
    try:
        chrome_options = Options()
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")  # 隱藏自動化標誌
        context.driver = webdriver.Chrome(options=chrome_options)
        context.driver.maximize_window()
        logger.info("Test 1 - Pass")
    except:
        logger.error("Test 1 - Fail")
        raise

@given(u'User navigates to the HexSchool main page')
def step_impl(context):
    try:
        context.driver.get("https://www.hexschool.com/")
        logger.info("Test 2 - Pass")
    except:
        logger.error("Test 2 - Fail")
        raise

@when(u'User clicks the "Login to Course Platform" button')
def step_impl(context):
    try:
        wait = WebDriverWait(context.driver, timeout=2)
        element1 = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'登入課程平台')]")))
        assert element1.is_displayed()

        ActionChains(context.driver).scroll_to_element(element1).perform()
        context.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center', inline: 'center'});",
                                  element1)

        ActionChains(context.driver).click(element1).perform()
        time.sleep(5)
        logger.info("Test 3 - Pass")
    except:
        logger.error("Test 3 - Fail")
        raise

@when(u'User clicks the "Teachable" link')
def step_impl(context):
    try:
        wait = WebDriverWait(context.driver, timeout=2)
        element1 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[class='login-block bg-light text-secondary rounded d-flex flex-column h-100'] img[class='img-fluid']")))
        assert element1.is_displayed()

        ActionChains(context.driver).scroll_to_element(element1).perform()
        context.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center', inline: 'center'});",
                                  element1)
        # 記錄原始窗口句柄
        context.original_window = context.driver.current_window_handle
        print(f"原始窗口句柄: {context.original_window}")

        ActionChains(context.driver).click(element1).perform()
        time.sleep(3)

        # 等待新標籤頁出現（最多等待 10 秒）
        wait = WebDriverWait(context.driver, 10)
        wait.until(EC.number_of_windows_to_be(2))  # 等待窗口數量變為 2

        # 獲取所有窗口句柄
        all_windows = context.driver.window_handles
        print(f"所有窗口句柄: {all_windows}")

        # 切換到新標籤頁
        for window_handle in all_windows:
            if window_handle != context.original_window:
                context.driver.switch_to.window(window_handle)
                break

        # 驗證新標籤頁的 URL
        new_url = context.driver.current_url
        print(f"當前 URL: {new_url}")

        logger.info("Test 4 - Pass")
    except:
        logger.error("Test 4 - Fail")
        raise

@when(u'User enters the email {Email}')
def step_impl(context, Email):
    try:
        wait = WebDriverWait(context.driver,10)
        element1 = wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@id='account']")))
        element1.click()
        element1.send_keys(Email)
        time.sleep(2)
        logger.info("Test 5 - Pass")
    except:
        logger.error("Test 5 - Fail")
        raise

@when(u'User enters the password {Password}')
def step_impl(context, Password):
    try:
        wait = WebDriverWait(context.driver, 10)
        element2 = wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@id='password']")))
        element2.click()
        element2.send_keys(Password)
        time.sleep(2)
        logger.info("Test 6 - Pass")
    except:
        logger.error("Test 6 - Fail")
        raise


@when(u'User clicks the Consent Button')
def step_impl(context):
    try:
        wait = WebDriverWait(context.driver, 10)
        element2 = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
        element2.click()

        time.sleep(2)
        logger.info("Test 7 - Pass")
    except:
        logger.error("Test 7 - Fail")
        raise


@when(u'User quits the browser')
def step_impl(context):
    try:
        time.sleep(5)
        # 可選：切換回原始標籤頁
        context.driver.switch_to.window(context.original_window)
        print(f"回到原始標籤頁 URL: {context.driver.current_url}")

        # 清理多餘窗口
        all_windows = context.driver.window_handles
        if len(all_windows) > 1:
            for window in all_windows[1:]:
                context.driver.switch_to.window(window)
                context.driver.close()
            context.driver.switch_to.window(all_windows[0])
        print(f"清理後窗口數量: {len(context.driver.window_handles)}")
        logger.info("Test 8 - Pass")
    except:
        logger.error("Test 8 - Fail")
        raise


@then(u'The signup process should be completed successfully')
def step_impl(context):
    try:
        print("The User Successful his test")
        context.driver.quit()
        logger.info("Test 9 - Pass")
    except:
        logger.error("Test 9 - Fail")
    raise


