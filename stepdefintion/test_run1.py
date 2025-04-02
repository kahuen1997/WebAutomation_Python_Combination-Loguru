import sys
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from loguru import logger
from selenium.webdriver.support import wait
from selenium.webdriver.support.wait import WebDriverWait


#Regression 1-13

@pytest.mark.regression
@pytest.mark.header
def test_p1(setup_and_teardown): #行事曆Tab
    driver = setup_and_teardown
    try:
        element = driver.find_element(by=By.XPATH, value="//span[contains(text(),'行事曆')]")
        assert element.is_displayed()
        element.click()
        logger.info("Task 1 Pass")
        # try:
        #     driver = setup_and_teardown
        #     element = driver.find_element(by=By.XPATH, value="//a[normalize-space()='List reporter']")
        #     assert element.is_displayed()
        #     element.click()
        #     logger.info("This test is a pass")
        # except:
        #     logger.error("This test is a fail")
    except:
        logger.error("Task 1 Error")
        raise
@pytest.mark.regression
@pytest.mark.header
def test_p2(setup_and_teardown): #精選課程Tab
    driver = setup_and_teardown
    try:
        element = driver.find_element(by=By.XPATH, value="//span[contains(text(),'精選課程')]")
        assert element.is_displayed()
        element.click()
        logger.info("Task 2 Pass")

    except:
        logger.error("Task 2 Error")
        raise

@pytest.mark.regression
@pytest.mark.header
def test_p3(setup_and_teardown): #企業方案Tab
    driver = setup_and_teardown
    try:
        element = driver.find_element(by=By.XPATH, value="//span[contains(text(),'企業方案')]")
        assert element.is_displayed()
        element.click()
        logger.info("Task 3 Pass")

    except:
        logger.error("Task 3 Error")
        raise

@pytest.mark.regression
@pytest.mark.header
def test_p4(setup_and_teardown): #部落格Tab
    driver = setup_and_teardown
    try:
        element = driver.find_element(by=By.XPATH, value="//span[contains(text(),'部落格')]")
        assert element.is_displayed()
        element.click()
        logger.info("Task 4 Pass")

    except:
        logger.error("Task 4 Error")
        raise

@pytest.mark.regression
@pytest.mark.header
def test_p5(setup_and_teardown): #問與答Tab
    driver = setup_and_teardown
    try:
        element = driver.find_element(by=By.XPATH, value="//span[contains(text(),'問與答')]")
        assert element.is_displayed()
        element.click()
        logger.info("Task 5 Pass")

    except:
        logger.error("Task 5 Error")
        raise

@pytest.mark.skip
def test_p6(setup_and_teardown): #問與答 - link
    driver = setup_and_teardown
    try:
        element = driver.find_element(by=By.XPATH, value="//p[contains(text(),'Q: 請問六角學院上課模式？')]")
        assert element.is_displayed()
        element.click()
        logger.info("Task 6 Pass")

    except:
        logger.error("Task 6 Error")
        raise

@pytest.mark.regression
def test_p7(setup_and_teardown): #Line Button
    driver = setup_and_teardown
    try:
        # 記錄原始窗口句柄
        original_window = driver.current_window_handle
        print(f"原始窗口句柄: {original_window}")

        # 神跡
        element = driver.find_element(by=By.XPATH, value="//a[@class='fab-icon fab fab-line d-none d-md-flex align-items-center justify-content-center mp-click line-track']")
        img_element = element.find_element(By.TAG_NAME, "img")
        img_element.click()
        # assert element.is_displayed()
        element.click()

        # 等待新標籤頁出現（最多等待 10 秒）
        wait = WebDriverWait(driver, 10)
        wait.until(EC.number_of_windows_to_be(3))  # 等待窗口數量變為 3

        # 獲取所有窗口句柄
        all_windows = driver.window_handles
        print(f"所有窗口句柄: {all_windows}")

        # 切換到新標籤頁
        for window_handle in all_windows:
            if window_handle != original_window:
                driver.switch_to.window(window_handle)
                break

        # 驗證新標籤頁的 URL
        new_url = driver.current_url
        print(f"當前 URL: {new_url}")

        # 在新標籤頁上操作（例如檢查標題）
        wait.until(EC.title_contains("LINE Login"))  # 替換為實際標題的一部分
        print(f"新標籤頁標題: {driver.title}")

        # 可選：切換回原始標籤頁
        driver.switch_to.window(original_window)
        print(f"回到原始標籤頁 URL: {driver.current_url}")

        logger.info("Task 7 Pass")


    except:
        logger.error("Task 7 Error")
        raise

@pytest.mark.regression
@pytest.mark.header
def test_p8(setup_and_teardown): #登入課程平台Tab
    driver = setup_and_teardown
    try:
        element = driver.find_element(by=By.XPATH, value="//span[contains(text(),'登入課程平台')]")
        assert element.is_displayed()
        element.click()

        # 等待模態對話框可見
        wait = WebDriverWait(driver, 10)
        modal = wait.until(
            EC.visibility_of_element_located((By.ID, "loginModal"))
        )

        h3_element = wait.until(
            EC.visibility_of_element_located((By.XPATH, "//h3[@class='text-dark' and text()='登入課程平台']"))
        )
        assert h3_element.is_displayed()

        close_button = wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "btn-close"))
        )
        close_button.click()

        # 可選：驗證模態對話框是否關閉
        wait.until(
            EC.invisibility_of_element_located((By.ID, "loginModal"))
        )

        logger.info("Task 8 Pass")

    except:
        logger.error("Task 8 Error")
        raise

@pytest.mark.regression
@pytest.mark.header
def test_p9(setup_and_teardown): #問與答 - 如何成為前端工程師
    driver = setup_and_teardown
    try:
        element = driver.find_element(by=By.XPATH, value="//span[contains(text(),'問與答')]")
        ActionChains(driver) \
            .move_to_element(element) \
            .perform()

        element1 = driver.find_element(by=By.XPATH,value="//a[@class='dropdown-item'][contains(text(),'如何成為前端工程師')]")
        element1.click()
        logger.info("Task 9 Pass")

    except:
        logger.error("Task 9 Error")
        raise
@pytest.mark.regression
@pytest.mark.header
def test_p10(setup_and_teardown): #問與答 - 六角學員作品牆
    driver = setup_and_teardown
    try:
        # 清理多餘窗口
        all_windows = driver.window_handles
        if len(all_windows) > 1:
            for window in all_windows[1:]:
                driver.switch_to.window(window)
                driver.close()
            driver.switch_to.window(all_windows[0])
        print(f"清理後窗口數量: {len(driver.window_handles)}")

        # 記錄原始窗口句柄
        original_window = driver.current_window_handle
        print(f"原始窗口句柄: {original_window}")

        # 假設點擊某個連結開啟新標籤頁（替換為實際的定位）
        element = driver.find_element(by=By.XPATH, value="//span[contains(text(),'問與答')]")
        ActionChains(driver) \
            .move_to_element(element) \
            .perform()

        element1 = driver.find_element(by=By.XPATH,value="//a[contains(text(),'六角學員作品牆')]")
        element1.click()

        # 等待新標籤頁出現（最多等待 20 秒）
        wait = WebDriverWait(driver, 20)
        wait.until(EC.number_of_windows_to_be(2))  # 等待窗口數量變為 2

        # 獲取所有窗口句柄
        all_windows = driver.window_handles
        print(f"所有窗口句柄: {all_windows}")

        # 切換到新標籤頁
        for window_handle in all_windows:
            if window_handle != original_window:
                driver.switch_to.window(window_handle)
                break

        # 驗證新標籤頁的 URL
        new_url = driver.current_url
        print(f"當前 URL: {new_url}")
        assert "https://works.hexschool.io" in new_url, "未成功切換到新標籤頁"

        # 在新標籤頁上操作（例如檢查標題）
        wait.until(EC.title_contains("六角學院作品牆"))  # 替換為實際標題的一部分
        print(f"新標籤頁標題: {driver.title}")

        # 點擊 "Vue" 連結
        newelement = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[normalize-space()='Vue']")
        ))
        newelement.click()
        # newelement = driver.find_element(by=By.XPATH,value="//a[normalize-space()='Vue']")
        # newelement.click()

        # 可選：切換回原始標籤頁
        driver.switch_to.window(original_window)
        print(f"回到原始標籤頁 URL: {driver.current_url}")

        logger.info("Task 10 Pass")

    except:
        logger.error("Task 10 Error")
        raise

@pytest.mark.regression
@pytest.mark.header
def test_p11(setup_and_teardown): #問與答 - 常見問答
    driver = setup_and_teardown
    try:
        element = driver.find_element(by=By.XPATH, value="//span[contains(text(),'問與答')]")
        ActionChains(driver) \
            .move_to_element(element) \
            .perform()

        element1 = driver.find_element(by=By.XPATH,value="//a[contains(text(),'常見問答')]")
        element1.click()
        logger.info("Task 11 Pass")

    except:
        logger.error("Task 11 Error")
        raise

@pytest.mark.regression
@pytest.mark.header
def test_p12(setup_and_teardown): #企業方案 - 企業教育訓練
    driver = setup_and_teardown
    try:
        element = driver.find_element(by=By.XPATH, value="//span[contains(text(),'企業方案')]")
        ActionChains(driver) \
            .move_to_element(element) \
            .perform()

        element1 = driver.find_element(by=By.XPATH,value="//a[contains(text(),'企業教育訓練')]")
        element1.click()
        logger.info("Task 12 Pass")

    except:
        logger.error("Task 12 Error")
        raise

@pytest.mark.regression
@pytest.mark.header
def test_p13(setup_and_teardown): #企業方案 - 廠商發案服務
    driver = setup_and_teardown
    try:
        element = driver.find_element(by=By.XPATH, value="//span[contains(text(),'企業方案')]")
        ActionChains(driver) \
            .move_to_element(element) \
            .perform()

        element1 = driver.find_element(by=By.XPATH,value="//a[contains(text(),'廠商發案服務')]")
        element1.click()
        logger.info("Task 13 Pass")

    except:
        logger.error("Task 13 Error")
        raise

@pytest.mark.smoke
@pytest.mark.header
def test_p14(setup_and_teardown): #精選課程
    driver = setup_and_teardown
    try:
        element = driver.find_element(by=By.XPATH, value="//span[contains(text(),'精選課程')]")
        ActionChains(driver) \
            .move_to_element(element) \
            .perform()

        element1 = driver.find_element(by=By.XPATH,value="/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[2]/a[1]/div[1]")
        element1.click()
        element1.click()

        element2 = driver.find_element(by=By.XPATH,value="/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[3]/a[1]/div[1]")
        element2.click()

        element3 = driver.find_element(by=By.XPATH,value="/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[4]/a[1]/div[1]")
        element3.click()

        element4 = driver.find_element(by=By.XPATH,value="/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[5]/a[1]/div[1]")
        element4.click()

        element5 = driver.find_element(by=By.XPATH,value="/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[6]/a[1]/div[1]")
        element5.click()
        element5.click()

        element6 = driver.find_element(by=By.XPATH,value="/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[7]/a[1]/div[1]")
        element6.click()

        logger.info("Task 14 Pass")

    except:
        logger.error("Task 14 Error")
        raise


