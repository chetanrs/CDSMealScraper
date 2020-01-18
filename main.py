from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import csv
import time

# a third comment to test something
month = "01"
day = "20"

driver = webdriver.Chrome()
driver.get("https://dining.unc.edu/locations/top-of-lenoir/?date=2020-" + month + "-" + day)

links = driver.find_elements_by_class_name("show-nutrition")

items_to_traverse = 50
item_count = 0
nutritional_labels = ["Item",
                      "Calories",
                      "Calories From Fat",
                      "Total Fat (g)",
                      "Saturated Fat (g)",
                      "Trans Fat (g)",
                      "Cholesterol (mg)",
                      "Sodium (mg)",
                      "Total Carbohydrate (g)",
                      "Dietary Fiber (g)",
                      "Sugars (g)",
                      "Protein (g)"]

with open('items.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(nutritional_labels)

    for link in links:
        if not link.is_displayed() or item_count == items_to_traverse:
            break

        link.click()

        try:
            nutrition = driver.find_element_by_id("nutrition-slider-stage").find_element_by_css_selector("div").text.splitlines()
        except NoSuchElementException:
            time.sleep(0.1)

        row_to_append = [nutrition[0]]
        for i in range(5, 16):
            for num in nutrition[i].split():
                try:
                    row_to_append.append(float(num))
                except ValueError:
                    pass

        writer.writerow(row_to_append)

        driver.find_element_by_class_name("close-nutrition").click()
        item_count += 1

driver.quit()