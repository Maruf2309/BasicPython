from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize the WebDriver
driver = webdriver.Chrome()

# Maximize the browser window
driver.maximize_window()

# List to store product links
link_list = []

# Loop through the pages
for page in range(1, 3):
    # Navigate to the page
    driver.get(f"https://www.daraz.com.bd/men-muslimin-shirts/?page={page}")
    time.sleep(3)  # Wait for the page to load

    # Determine the number of items on the current page
    if page == 1:
        num_items = 40
    else:
        num_items = 27

    # Loop through the items on the current page
    for i in range(1, num_items + 1):
        try:
            # Construct the XPath for the item
            xpath = f'//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[2]/div[{i}]/div/div/div[2]/div[2]/a'
            # Find the element and get the href attribute
            link = driver.find_element(By.XPATH, xpath).get_attribute('href')
            # Append the link to the list
            link_list.append(link)
        except Exception as e:
            print(f"Error on page {page}, item {i}: {e}")

# Print the collected links
for link in link_list:
    print(link)


# Print the total number of items found
print(f"Total number of items found: {len(link_list)}")

# Close the WebDriver
driver.quit()




