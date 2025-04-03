import logging
import time

import pytest
from loguru import logger
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
@pytest.mark.regression
@pytest.mark.mainpage
def test_m1(setup_and_teardown):
    try:
        driver = setup_and_teardown
        # 等待模態對話框可見
        wait = WebDriverWait(driver, 10)
        modal = wait.until(
            EC.visibility_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/nav[1]/div[1]/h1[1]/a[1]"))
        )

        assert modal.is_displayed()
        logger.info("Main Page Task 1 Pass")
    except:
        logger.error("Main Page Task 1 Fail")

@pytest.mark.regression
@pytest.mark.mainpage
def test_m2(setup_and_teardown):
    try:
        driver = setup_and_teardown
        # 等待模態對話框可見
        element = driver.find_element(by=By.XPATH, value="/html[1]/body[1]/div[3]/div[4]/div[1]/div[1]/div[1]/h2[1]")

        ActionChains(driver) \
            .scroll_to_element(element) \
            .perform()
        assert element.is_displayed()

        element1 = driver.find_element(by=By.XPATH, value="//a[contains(text(),'看更多評論')]")
        ActionChains(driver) \
            .double_click(element1) \
            .perform()
        print(f"Click")

        driver.back()

        logger.info("Main Page Task 2 Pass")
    except:
        logger.error("Main Page Task 2 Fail")
        raise

@pytest.mark.regression
@pytest.mark.mainpage
def test_m3(setup_and_teardown):
    try:
        driver = setup_and_teardown
        # 等待模態對話框可見
        element1 = driver.find_element(by=By.CSS_SELECTOR, value="div[class='beveled-images-layout pt-md-7 pt-5 text-dark bg-md-light-reverse'] h2[class='font-section-title align-self-md-center align-self-start']")

        ActionChains(driver) \
            .scroll_to_element(element1) \
            .perform()
        assert element1.is_displayed()

        element2 = driver.find_element(by=By.XPATH, value="//i[@class='material-icons'][normalize-space()='arrow_forward']")
        for _ in range(3):
            element2.click()
            time.sleep(2)

        element3 = driver.find_element(by=By.XPATH, value="//i[normalize-space()='arrow_back']")
        for _ in range(3):
            element3.click()
            time.sleep(2)

        # 記錄原始窗口句柄
        original_window = driver.current_window_handle
        print(f"原始窗口句柄: {original_window}")

        element4 = driver.find_element(by=By.XPATH, value="//a[@class='custom-swiper-slide swiper-slide my-2 swiper-slide-active']")
        element4.click()

        # 等待新標籤頁出現（最多等待 10 秒）
        wait = WebDriverWait(driver, 10)
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

        # 可選：切換回原始標籤頁
        driver.switch_to.window(original_window)
        print(f"回到原始標籤頁 URL: {driver.current_url}")

        # 清理多餘窗口
        all_windows = driver.window_handles
        if len(all_windows) > 1:
            for window in all_windows[1:]:
                driver.switch_to.window(window)
                driver.close()
            driver.switch_to.window(all_windows[0])
        print(f"清理後窗口數量: {len(driver.window_handles)}")

        logging.info("Main Page Task 3 Pass")
    except:
        logging.error("Main Page Task 3 Fail")
        raise

@pytest.mark.regression
@pytest.mark.mainpage
def test_m4(setup_and_teardown):
    try:
        driver = setup_and_teardown

        element = driver.find_element(by=By.XPATH, value="//h2[@class='mb-0 text-center text-divider text-dark text-w-lighter']")
        ActionChains(driver) \
            .scroll_to_element(element) \
            .perform()
        assert element.is_displayed()

        element1 = driver.find_element(by=By.XPATH, value="//div[@class='beveled-images-layout pt-md-7 pt-5 text-dark bg-md-light-reverse']//div[1]//a[1]//div[1]")
        element1.click()

        driver.back()

        element2 = driver.find_element(by=By.XPATH,value="//div[@class='mt-4 img-layout-overflow img-layout-md-overflow']//div[2]//a[1]//div[1]")
        element2.click()

        driver.back()

        wait = WebDriverWait(driver, 10)
        # 定位並點擊元素
        element3 = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//div//div[3]//a[1]//div[1]"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", element3)  # 確保可見
        element3.click()

        driver.back()

        element4 = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//div//div[4]//a[1]//div[1]"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", element4)  # 確保可見
        element4.click()

        driver.back()

        element5 = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//div//div[5]//a[1]//div[1]"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", element5)  # 確保可見
        element5.click()

        driver.back()

        element6 = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//div//div[6]//a[1]//div[1]"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", element6)  # 確保可見
        element6.click()

        driver.back()

        element7 = driver.find_element(by=By.XPATH, value="//a[contains(text(),'求職故事')]")
        element7.click()

        driver.back()

        logger.info("Main Page Task 4 Pass")
    except:
        logger.error("Main Page Task 4 Fail")
        raise

@pytest.mark.regression
@pytest.mark.mainpage
def test_m5(setup_and_teardown):
    try:
        driver = setup_and_teardown
        wait = WebDriverWait(driver, 10)
        element1 = wait.until(
            EC.visibility_of_element_located((By.XPATH,"//h4[contains(text(),'我想學網頁設計 🔥')]"))
        )
        ActionChains(driver).scroll_to_element(element1).perform()
        driver.execute_script("arguments[0].scrollIntoView(true);", element1)
        assert element1.is_displayed()

        time.sleep(2)
        # --------------------------------------------------------------------------------------
        # 記錄原始窗口句柄
        original_window = driver.current_window_handle
        print(f"原始窗口句柄: {original_window}")

        element2 = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(@class,'course-straight z_bs4_html_jquery_rwd')]//a[contains(@class,'text-muted')][contains(text(),'使用 HTML、CSS 開發一個網站')]"))
        )
        ActionChains(driver).scroll_to_element(element2).perform()
        driver.execute_script("arguments[0].scrollIntoView(true);", element2)
        assert  element2.is_displayed()
        element2.click()

        # 等待新標籤頁出現（最多等待 10 秒）
        wait = WebDriverWait(driver, 10)
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

        # 可選：切換回原始標籤頁
        driver.switch_to.window(original_window)
        print(f"回到原始標籤頁 URL: {driver.current_url}")

        # 清理多餘窗口
        all_windows = driver.window_handles
        if len(all_windows) > 1:
            for window in all_windows[1:]:
                driver.switch_to.window(window)
                driver.close()
            driver.switch_to.window(all_windows[0])
        print(f"清理後窗口數量: {len(driver.window_handles)}")
        # --------------------------------------------------------------------------------------
        # 記錄原始窗口句柄
        original_window = driver.current_window_handle
        print(f"原始窗口句柄: {original_window}")

        element3 = wait.until(
            EC.element_to_be_clickable((By.XPATH,
                                        "//div[contains(@class,'course-straight z_bs4_html_jquery_rwd')]//a[contains(@class,'text-muted')][contains(text(),'jQuery 網頁互動效果')]"))
        )
        ActionChains(driver).scroll_to_element(element3).perform()
        driver.execute_script("arguments[0].scrollIntoView(true);", element3)
        assert element3.is_displayed()
        element3.click()

        # 等待新標籤頁出現（最多等待 10 秒）
        wait = WebDriverWait(driver, 10)
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

        # 可選：切換回原始標籤頁
        driver.switch_to.window(original_window)
        print(f"回到原始標籤頁 URL: {driver.current_url}")

        # 清理多餘窗口
        all_windows = driver.window_handles
        if len(all_windows) > 1:
            for window in all_windows[1:]:
                driver.switch_to.window(window)
                driver.close()
            driver.switch_to.window(all_windows[0])
        print(f"清理後窗口數量: {len(driver.window_handles)}")

        # --------------------------------------------------------------------------------------
        # 記錄原始窗口句柄
        original_window = driver.current_window_handle
        print(f"原始窗口句柄: {original_window}")

        element4 = wait.until(
            EC.element_to_be_clickable((By.XPATH,
                                        "//div[contains(@class,'course-straight z_bs4_html_jquery_rwd')]//a[contains(@class,'text-muted')][contains(text(),'一變應萬變的響應式網頁設計')]"))
        )
        ActionChains(driver).scroll_to_element(element4).perform()
        driver.execute_script("arguments[0].scrollIntoView(true);", element4)
        assert element4.is_displayed()
        element4.click()

        # 等待新標籤頁出現（最多等待 10 秒）
        wait = WebDriverWait(driver, 10)
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

        # 可選：切換回原始標籤頁
        driver.switch_to.window(original_window)
        print(f"回到原始標籤頁 URL: {driver.current_url}")

        # 清理多餘窗口
        all_windows = driver.window_handles
        if len(all_windows) > 1:
            for window in all_windows[1:]:
                driver.switch_to.window(window)
                driver.close()
            driver.switch_to.window(all_windows[0])
        print(f"清理後窗口數量: {len(driver.window_handles)}")

        # --------------------------------------------------------------------------------------
        # 記錄原始窗口句柄
        original_window = driver.current_window_handle
        print(f"原始窗口句柄: {original_window}")

        element5 = wait.until(
            EC.element_to_be_clickable((By.XPATH,
                                        "//div[contains(@class,'course-straight z_bs4_html_jquery_rwd')]//a[contains(@class,'text-muted')][contains(text(),'Bootstrap 5 網頁切版整合術')]"))
        )
        ActionChains(driver).scroll_to_element(element5).perform()
        driver.execute_script("arguments[0].scrollIntoView(true);", element5)
        assert element5.is_displayed()
        element5.click()

        # 等待新標籤頁出現（最多等待 10 秒）
        wait = WebDriverWait(driver, 10)
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

        # 可選：切換回原始標籤頁
        driver.switch_to.window(original_window)
        print(f"回到原始標籤頁 URL: {driver.current_url}")

        # 清理多餘窗口
        all_windows = driver.window_handles
        if len(all_windows) > 1:
            for window in all_windows[1:]:
                driver.switch_to.window(window)
                driver.close()
            driver.switch_to.window(all_windows[0])
        print(f"清理後窗口數量: {len(driver.window_handles)}")

        logger.info("Main Page Task 5 Pass")
    except:
        logger.error("Main Page Task 5 Fail")
        raise

@pytest.mark.regression
@pytest.mark.mainpage
def test_m6(setup_and_teardown):
    try:
        driver = setup_and_teardown
        wait = WebDriverWait(driver,10)
        element1 = wait.until(
            EC.visibility_of_element_located((By.XPATH,"//select[contains(@class,'form-select bg-white px-3 py-0 font-weight-bold rounded-0 mb-3 course-straight-select z_js-plus_js-core_vue3')]"))
        )
        assert element1.is_displayed()
        ActionChains(driver).scroll_to_element(element1).perform()
        driver.execute_script("arguments[0].scrollIntoView(true);", element1)
        time.sleep(3)
        select = Select(element1)
        select.select_by_index(1)

 # --------------------------------------------------------------------------------------
        # 記錄原始窗口句柄
        original_window = driver.current_window_handle
        print(f"原始窗口句柄: {original_window}")

        element2 = wait.until(
            EC.element_to_be_clickable((By.XPATH,
                                        "//div[contains(@class,'course-straight z_js-js_core-react')]//a[contains(@class,'text-muted')][contains(text(),'React 實戰影音課程')]"))
        )
        ActionChains(driver).scroll_to_element(element2).perform()
        driver.execute_script("arguments[0].scrollIntoView(true);", element2)
        assert element2.is_displayed()
        element2.click()

        # 等待新標籤頁出現（最多等待 10 秒）
        wait = WebDriverWait(driver, 10)
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

        # 可選：切換回原始標籤頁
        driver.switch_to.window(original_window)
        print(f"回到原始標籤頁 URL: {driver.current_url}")

        # 清理多餘窗口
        all_windows = driver.window_handles
        if len(all_windows) > 1:
            for window in all_windows[1:]:
                driver.switch_to.window(window)
                driver.close()
            driver.switch_to.window(all_windows[0])
        print(f"清理後窗口數量: {len(driver.window_handles)}")

        # --------------------------------------------------------------------------------------
        # 記錄原始窗口句柄
        original_window = driver.current_window_handle
        print(f"原始窗口句柄: {original_window}")

        element2 = wait.until(
            EC.element_to_be_clickable((By.XPATH,
                                        "//div[contains(@class,'course-straight z_js-js_core-react')]//a[contains(@class,'text-muted')][contains(text(),'JavaScript 前端修練全攻略')]"))
        )
        ActionChains(driver).scroll_to_element(element2).perform()
        driver.execute_script("arguments[0].scrollIntoView(true);", element2)
        assert element2.is_displayed()
        element2.click()

        # 等待新標籤頁出現（最多等待 10 秒）
        wait = WebDriverWait(driver, 10)
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

        # 可選：切換回原始標籤頁
        driver.switch_to.window(original_window)
        print(f"回到原始標籤頁 URL: {driver.current_url}")

        # 清理多餘窗口
        all_windows = driver.window_handles
        if len(all_windows) > 1:
            for window in all_windows[1:]:
                driver.switch_to.window(window)
                driver.close()
            driver.switch_to.window(all_windows[0])
        print(f"清理後窗口數量: {len(driver.window_handles)}")

        # --------------------------------------------------------------------------------------
        # 記錄原始窗口句柄
        original_window = driver.current_window_handle
        print(f"原始窗口句柄: {original_window}")

        element2 = wait.until(
            EC.element_to_be_clickable((By.XPATH,
                                        "//div[contains(@class,'course-straight z_js-js_core-react')]//a[contains(@class,'text-muted')][contains(text(),'JavaScript - 核心篇')]"))
        )
        ActionChains(driver).scroll_to_element(element2).perform()
        driver.execute_script("arguments[0].scrollIntoView(true);", element2)
        assert element2.is_displayed()
        element2.click()

        # 等待新標籤頁出現（最多等待 10 秒）
        wait = WebDriverWait(driver, 10)
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

        # 可選：切換回原始標籤頁
        driver.switch_to.window(original_window)
        print(f"回到原始標籤頁 URL: {driver.current_url}")

        # 清理多餘窗口
        all_windows = driver.window_handles
        if len(all_windows) > 1:
            for window in all_windows[1:]:
                driver.switch_to.window(window)
                driver.close()
            driver.switch_to.window(all_windows[0])
        print(f"清理後窗口數量: {len(driver.window_handles)}")

        logger.info("Main Page Task 5 Pass")
    except:
        logger.error("Main Page Task 5 Fail")
        raise


