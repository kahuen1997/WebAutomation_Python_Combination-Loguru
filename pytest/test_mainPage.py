import logging
import time

import pyautogui
import pytest
from loguru import logger
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
@pytest.mark.regression
@pytest.mark.mainpage
def test_m1(setup_and_teardown): #六角學院title
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
def test_m2(setup_and_teardown): #看更多評論 title
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
def test_m3(setup_and_teardown): #學員作品
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
def test_m4(setup_and_teardown):  #不論你是任何背景，六角都有成功案例！
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

@pytest.mark.regression #影音課程方案推薦 (1)
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

@pytest.mark.regression #影音課程方案推薦 (2)
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
        time.sleep(2)
        select.select_by_index(0)

 # --------------------------------------------------------------------------------------
        # 記錄原始窗口句柄
        original_window = driver.current_window_handle
        print(f"原始窗口句柄: {original_window}")

        element2 = wait.until(
            EC.element_to_be_clickable((By.XPATH,
                                        "//div[@class='course-straight z_js-plus_js-core_vue3']//a[@class='text-muted'][contains(text(),'Vue 3 實戰影音課程')]"))
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

        element3 = wait.until(
            EC.element_to_be_clickable((By.XPATH,
                                        "(//a[@class='text-muted'][contains(text(),'JavaScript 前端修練全攻略')])[1]"))
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
                                        "(//a[@class='text-muted'][contains(text(),'JavaScript - 核心篇')])[1]"))
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

        logger.info("Main Page Task 6 Pass")
    except:
        logger.error("Main Page Task 6 Fail")
        raise

@pytest.mark.regression #影音課程方案推薦 (3)
@pytest.mark.mainpage
def test_m7(setup_and_teardown):
    try:
        driver = setup_and_teardown
        wait = WebDriverWait(driver,10)
        element1 = wait.until(
            EC.visibility_of_element_located((By.XPATH,"//select[@class='form-select bg-white px-3 py-0 font-weight-bold rounded-0 mb-3 course-straight-select z_html_jQuery_rwd_bs4_js-plus_js-core_vue3']"))
        )
        assert element1.is_displayed()
        ActionChains(driver).scroll_to_element(element1).perform()
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center', inline: 'center'});", element1)
        time.sleep(3)
        select = Select(element1)
        select.select_by_index(1)
        time.sleep(2)
        select.select_by_index(0)
        # --------------------------------------------------------------------------------------
        # 記錄原始窗口句柄
        original_window = driver.current_window_handle
        print(f"原始窗口句柄: {original_window}")

        element2 = wait.until(
            EC.element_to_be_clickable((By.XPATH,
                                        "//div[contains(@class,'course-straight z_html_jQuery_rwd_bs4_js-plus_js-core_vue3')]//a[contains(@class,'text-muted')][contains(text(),'使用 HTML、CSS 開發一個網站')]"))
        )
        ActionChains(driver).scroll_to_element(element2).perform()
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center', inline: 'center'});", element2)
        time.sleep(2)
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

        element3 = wait.until(
            EC.element_to_be_clickable((By.XPATH,
                                        "//div[contains(@class,'course-straight z_html_jQuery_rwd_bs4_js-plus_js-core_vue3')]//a[contains(@class,'text-muted')][contains(text(),'jQuery 網頁互動效果')]"))
        )
        ActionChains(driver).scroll_to_element(element3).perform()
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center', inline: 'center'});", element3)
        time.sleep(2)
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
                                        "//div[contains(@class,'course-straight z_html_jQuery_rwd_bs4_js-plus_js-core_vue3')]//a[contains(@class,'text-muted')][contains(text(),'JavaScript 核心篇')]"))
        )
        ActionChains(driver).scroll_to_element(element4).perform()
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center', inline: 'center'});", element4)
        time.sleep(2)
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
                                        "//div[contains(@class,'course-straight z_html_jQuery_rwd_bs4_js-plus_js-core_vue3')]//a[contains(@class,'text-muted')][contains(text(),'一變應萬變的響應式網頁設計')]"))
        )
        ActionChains(driver).scroll_to_element(element5).perform()
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center', inline: 'center'});", element5)
        time.sleep(2)
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

        # --------------------------------------------------------------------------------------
        # 記錄原始窗口句柄
        original_window = driver.current_window_handle
        print(f"原始窗口句柄: {original_window}")

        element6 = wait.until(
            EC.element_to_be_clickable((By.XPATH,
                                        "//div[contains(@class,'course-straight z_html_jQuery_rwd_bs4_js-plus_js-core_vue3')]//a[contains(@class,'text-muted')][contains(text(),'Bootstrap 5 網頁切版整合術')]"))
        )
        ActionChains(driver).scroll_to_element(element6).perform()
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center', inline: 'center'});", element6)
        time.sleep(2)
        assert element6.is_displayed()
        element6.click()

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

        element7 = wait.until(
            EC.element_to_be_clickable((By.XPATH,
                                        "//div[contains(@class,'course-straight z_html_jQuery_rwd_bs4_js-plus_js-core_vue3')]//a[contains(@class,'text-muted')][contains(text(),'Vue 3 實戰影音課程')]"))
        )
        ActionChains(driver).scroll_to_element(element7).perform()
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center', inline: 'center'});", element7)
        time.sleep(2)
        assert element7.is_displayed()
        element7.click()

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

        logger.info("Main Page Task 7 Pass")

    except:
        logger.error("Main Page Task 7 Fail")
        raise


@pytest.mark.regression #付款上課去 button
@pytest.mark.mainpage
def test_m8(setup_and_teardown):
    try:
        driver = setup_and_teardown
        wait = WebDriverWait(driver,10)
        element1 = wait.until(
            EC.element_to_be_clickable((By.XPATH,"//a[contains(@title,'開啟 網頁切版組合包 支付流程')]"))
        )

        ActionChains(driver).scroll_to_element(element1).perform()

        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center', inline: 'center'});",
                              element1)
        time.sleep(2)
        assert element1.is_displayed()

        element1.click()

        element2 = wait.until(EC.visibility_of_element_located((By.XPATH, "//strong[contains(text(),'就算是小問題，我們也在線上立即回覆您。')]")))
        assert element2.is_displayed()

        ActionChains(driver).send_keys(Keys.ESCAPE).perform()

        # --------------------------------------------------------------------------------------
        element3 = wait.until(
            EC.element_to_be_clickable((By.XPATH,"//div[@class='course-straight z_html_jQuery_rwd_bs4_js-plus_js-core_vue3']//a[@title='開啟 前端全組合 (不含加購品) 支付流程'][contains(text(),'付款上課去')]"))
        )

        ActionChains(driver).scroll_to_element(element3).perform()

        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center', inline: 'center'});",
                              element3)
        time.sleep(2)
        assert element3.is_displayed()

        element3.click()

        element4 = wait.until(EC.visibility_of_element_located((By.XPATH, "//strong[contains(text(),'就算是小問題，我們也在線上立即回覆您。')]")))
        assert element4.is_displayed()

        ActionChains(driver).send_keys(Keys.ESCAPE).perform()

        # --------------------------------------------------------------------------------------
        element5 = wait.until(
            EC.element_to_be_clickable((By.XPATH,"//a[@title='開啟 JS 全攻略, JS 核心, Vue 組合包 支付流程']"))
        )

        ActionChains(driver).scroll_to_element(element5).perform()

        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center', inline: 'center'});",
                              element5)
        time.sleep(2)
        assert element5.is_displayed()

        element5.click()

        element6 = wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//strong[contains(text(),'就算是小問題，我們也在線上立即回覆您。')]")))
        assert element6.is_displayed()

        ActionChains(driver).move_by_offset(1, 1).click().perform()

        logger.info("Main Page Task 8 Pass")
    except:
        logger.error("Main Page Task 8 Fail")
        raise


@pytest.mark.regression #六角學習地圖
@pytest.mark.mainpage
def test_m9(setup_and_teardown):
    try:
        driver = setup_and_teardown

        wait = WebDriverWait(driver,10)
        element1 = wait.until(
            EC.element_to_be_clickable((By.XPATH,"//a[@class='text-dark']//img[@class='img-fluid']"))
        )
        ActionChains(driver).scroll_to_element(element1).perform()

        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center', inline: 'center'});",
                              element1)
        element1.click()
        time.sleep(2)

        element2 = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[@class='text-dark']//img[@class='img-fluid']"))
        )
        ActionChains(driver).scroll_to_element(element2).perform()

        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center', inline: 'center'});",
                              element2)

        element2.click()
        logger.info("Main Page Task 9 Pass")
    except:
        logger.error("Main Page Task 9 Fail")
        raise

@pytest.mark.regression #六角學習地圖 (2)
@pytest.mark.mainpage
def test_m10(setup_and_teardown):
    try:
        driver = setup_and_teardown
        wait = WebDriverWait(driver,10)
        element1 = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[name()='rect' and @id='map-node']")))
        ActionChains(driver).scroll_to_element(element1).perform()

        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center', inline: 'center'});",
                              element1)
        assert element1.is_displayed()
        time.sleep(2)

        # 記錄原始窗口句柄
        original_window = driver.current_window_handle
        print(f"原始窗口句柄: {original_window}")

        element1.click()

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
        logger.info("Main Page Task 10 Pass")
    except:
        logger.error("Main Page Task 10 Fail")
        raise

@pytest.mark.regression #前端開發者技能樹 / 我們聯絡 link
@pytest.mark.mainpage
def test_m11(setup_and_teardown):
    try:
        driver = setup_and_teardown
        wait = WebDriverWait(driver,10)
        element1 = wait.until(EC.element_to_be_clickable((By.XPATH,"//a[contains(text(),'前端開發者技能樹')]")))
        ActionChains(driver).scroll_to_element(element1).perform()
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center', inline: 'center'});",
                              element1)
        # 記錄原始窗口句柄
        original_window = driver.current_window_handle
        print(f"原始窗口句柄: {original_window}")

        element1.click()

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
        element2 = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='link-bg-line link-dark fb-track']")))
        ActionChains(driver).scroll_to_element(element2).perform()
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center', inline: 'center'});",
                              element2)
        # 記錄原始窗口句柄
        original_window = driver.current_window_handle
        print(f"原始窗口句柄: {original_window}")

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

        logger.info("Main Page Task 11 Pass")
    except:
        logger.error("Main Page Task 11 Fail")
        raise

@pytest.mark.regression #所有課程介紹 button
@pytest.mark.mainpage
def test_m12(setup_and_teardown):
    try:
        driver = setup_and_teardown
        wait = WebDriverWait(driver,10)
        element1 = wait.until(
            EC.element_to_be_clickable((By.XPATH, "(//a[contains(text(),'所有課程介紹')])[1]"))
        )

        # element2 = wait.until(
        #     EC.element_to_be_clickable((By.XPATH, "//h2[contains(text(),'想轉職成工程師嗎？')]"))
        # )
        assert element1.is_displayed()
        ActionChains(driver).scroll_to_element(element1).perform()

        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center', inline: 'center'});",
                              element1)

        time.sleep(2)
        element1.click()

        time.sleep(2)
        driver.back()

        logger.info("Main Page Task 12 Pass")
    except:
        logger.error("Main Page Task 12 Fail")
        raise


@pytest.mark.regression #想和我們談談你的人生規劃嗎？歡迎聯繫我們
@pytest.mark.mainpage
def test_m13(setup_and_teardown):
    try:
        driver = setup_and_teardown
        wait = WebDriverWait(driver, 10)
        element1 = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[@class='col-md-6 align-self-md-center']//img[@class='img-fluid']"))
        )
        ActionChains(driver).scroll_to_element(element1).perform()
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center', inline: 'center'});", element1)

        # 記錄原始窗口句柄
        original_window = driver.current_window_handle
        print(f"原始窗口句柄: {original_window}")

        element1.click()

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

        logger.info("Main Page Task 13 Pass")
    except:
        logger.error("Main Page Task 13 Fail")
        raise

@pytest.mark.regression
@pytest.mark.mainpage
def test_m13(setup_and_teardown):
    try:
        driver = setup_and_teardown
        wait = WebDriverWait(driver, 10)
        element1 = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='tel']"))
        )

        assert element1.is_displayed()

        ActionChains(driver).scroll_to_element(element1).perform()
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center', inline: 'center'});", element1)

        time.sleep(2)

        element1.click()

        time.sleep(3)

        # 設置 pyautogui 的安全模式
        pyautogui.FAILSAFE = True
        pyautogui.PAUSE = 0.5  # 每個動作間的間隔

        # # 獲取元素在瀏覽器中的位置
        # element_location = element1.location  # 相對於瀏覽器內容區域的座標
        # element_size = element1.size  # 元素的寬度和高度
        #
        # # 計算元素中心的相對座標
        # element_center_x = element_location['x'] + element_size['width'] // 2
        # element_center_y = element_location['y'] + element_size['height'] // 2
        #
        # # 獲取瀏覽器視窗在螢幕上的位置
        # window_position = driver.get_window_position()
        # window_x = window_position['x']
        # window_y = window_position['y']
        #
        # # 計算螢幕上的絕對座標
        # # 注意：需要加上瀏覽器邊框和工具列的偏移（根據作業系統和瀏覽器調整）
        # browser_offset_x = 10  # 瀏覽器左邊框的偏移（手動調整）
        # browser_offset_y = 100  # 瀏覽器標題列和工具列的偏移（手動調整）
        # screen_x = window_x + element_center_x + browser_offset_x
        # screen_y = window_y + element_center_y + browser_offset_y
        #
        # print(f"按鈕的螢幕座標：({screen_x}, {screen_y})")
        #
        # # 用 PyAutoGUI 點擊按鈕
        # pyautogui.click(screen_x, screen_y)
        # print("已點擊按鈕，觸發系統彈窗")
        #
        # # 等待系統彈窗出現
        # time.sleep(1)  # 根據實際情況調整
        #
        # # 找到「取消」按鈕的螢幕座標
        # # 方法 1：手動獲取「取消」按鈕的座標
        # print("請在 5 秒內將滑鼠移動到「取消」按鈕上")
        # time.sleep(5)
        # cancel_button_position = pyautogui.position()
        # print(f"「取消」按鈕的座標：{cancel_button_position}")
        #
        # # 用 PyAutoGUI 點擊「取消」按鈕
        # pyautogui.click(cancel_button_position)
        # print("已點擊「取消」按鈕")

        pyautogui.click(x=1230, y=309)

        # --------------------------------------------------------------------------------------
        element2 = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[@class='landing-line line-track d-none d-md-block']//button[contains(@class,'btn w-100 rounded-0 d-flex align-items-center justify-content-center py-4 font-section-sub-title')][normalize-space()='hexschool']"))
        )
        ActionChains(driver).scroll_to_element(element2).perform()
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center', inline: 'center'});",
                              element2)

        # 記錄原始窗口句柄
        original_window = driver.current_window_handle
        print(f"原始窗口句柄: {original_window}")

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

        logger.info("Main Page Task 13 Pass")
    except:
        logger.error("Main Page Task 13 Fail")
        raise