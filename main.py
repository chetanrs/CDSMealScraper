from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import csv
import time

month = "01"
day = "20"

driver = webdriver.Chrome()
driver.get("https://dining.unc.edu/locations/top-of-lenoir/?date=2020-" + month + "-" + day)

links = driver.find_elements_by_class_name("show-nutrition")

items_to_traverse = 5
item_count = 0
nutritional_labels = ["Calories: ",
                      "Calories from fat: ",
                      "Total Fat(g): ",
                      "Saturated Fat(g): ",
                      "Trans Fat(g): ",
                      "Cholesterol(mg): ",
                      "Sodium(mg): ",
                      "Total Carbohydrate(g): ",
                      "Dietary Fiber(g): ",
                      "Sugars(g): ",
                      "Protein(g): "]

for link in links:
    if not link.is_displayed() or item_count == items_to_traverse:
        break

    link.click()

    try:
        nutrition = driver.find_element_by_id("nutrition-slider-stage").find_element_by_css_selector("div").text.splitlines()
    except NoSuchElementException:
        time.sleep(0.1)

    print("Item: " + nutrition[0])
    for i in range(5, 16):
        for num in nutrition[i].split():
            try:
                print(nutritional_labels[i - 5] + str(float(num)))
            except ValueError:
                pass

    driver.find_element_by_class_name("close-nutrition").click()
    item_count += 1
    print("")

driver.quit()