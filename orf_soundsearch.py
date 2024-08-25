import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


def init_driver():
    driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    driver.set_window_size(1920, 1080)
    driver.maximize_window()
    return driver


def wait_and_click(driver, by, value, timeout=10):
    element = WebDriverWait(driver, timeout).until(ec.element_to_be_clickable((by, value)))
    driver.execute_script("arguments[0].scrollIntoView(true);", element)
    driver.execute_script("arguments[0].click();", element)
    return element


def count_stations(result_list, station_names):
    station_counts = {name: 0 for name in station_names}
    for item in result_list:
        results = item.find_elements(By.CSS_SELECTOR, "div.text > span")
        for result in results:
            title = result.get_attribute("title").strip()
            for station in station_names:
                if station in title:
                    station_counts[station] += 1
    return station_counts


def test_search_results():
    driver = init_driver()
    url = "https://sound.orf.at/"
    driver.get(url)

    try:
        try:
            wait_and_click(driver, By.ID, "didomi-notice-disagree-button")
        except Exception as e:
            print(f"Cookie notice not found or another issue: {e}")

        wait_and_click(driver, By.CSS_SELECTOR, "button.icon-button.open-search-button")
        search_field = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, "input[name=Suche]")))
        time.sleep(1)  #reduce bugs
        search_field.send_keys("Nachmittag")

        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, "div.search-results-container")))
        time.sleep(3)
        assert driver.find_element(By.CSS_SELECTOR, "div.search-results-container"), \
            "Search results container not found"

        result_container = driver.find_element(By.CSS_SELECTOR, "div.search-results-container")
        result_list = result_container.find_elements(By.CSS_SELECTOR, "div.footer-container.footer-container-with-text")
        print(f"\n\nFound {len(result_list)} results")

        station_names = ["Hitradio Ö3", "Ö1", "radio FM4", "Radio Wien", "Radio NÖ", "Radio Burgenland", "Radio OÖ",
                         "Radio Tirol", "Radio Vorarlberg", "Radio Steiermark", "Radio Salzburg", "Ö1 Campus",
                         "Radio Kärnten"]

        station_counts = count_stations(result_list, station_names)
        for station, count1 in station_counts.items():
            if count1 > 0:
                print(f"Radio {station}: {count1}")

        station_counts = count_stations(result_list, station_names)
        assert sum(1 for count in station_counts.values() if count > 0) > 1, \
            "Expected results from more than one station"

        wait_and_click(driver, By.CSS_SELECTOR, "button.button.s-32.secondary")
        wait_and_click(driver, By.XPATH, "//button[text()='Radio Kärnten']")
        wait_and_click(driver, By.CSS_SELECTOR, "button.button.s-32.primary.apply-filter-button")
        time.sleep(5)

        print("_" * 20)
        result_list = result_container.find_elements(By.CSS_SELECTOR, "div.footer-container.footer-container-with-text")
        print(f"Found {len(result_list)} results")
        station_counts = count_stations(result_list, station_names)
        for station, count1 in station_counts.items():
            if count1 > 0:
                print(f"Radio {station}: {count1}")

        station_counts = count_stations(result_list, station_names)
        assert all(count == 0 or station == "Radio Kärnten" for station, count in station_counts.items()), \
            "Results contain stations other than 'Radio Kärnten'"
    finally:
        driver.quit()


test_search_results()