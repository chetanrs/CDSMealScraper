from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://dining.unc.edu/locations/top-of-lenoir/?date=2020-01-07")

links = driver.find_elements_by_class_name("show-nutrition")

items_to_traverse = 20
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
    time.sleep(0.15)

    nutrition = driver.find_element_by_id("nutrition-slider-stage").find_element_by_css_selector(
        "div").text.splitlines()

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
