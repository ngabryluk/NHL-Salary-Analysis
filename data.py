from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time
import pdb

# Set up Chrome WebDriver (make sure to point to your chromedriver location if it's not in PATH)
driver_path = '/path/to/chromedriver'  # Replace with your path
driver = webdriver.Chrome(executable_path=driver_path)

# Open the website
url = 'https://dashboard.puckpedia.com/?q=KEEYVU'
driver.get(url)

# Wait for the page to fully load (increase time if needed)
time.sleep(5)

# Get page source and parse with BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Close the browser
driver.quit()

# Find all tables and extract them into a Pandas DataFrame
tables = pd.read_html(str(soup))
df = tables[0]  # Assuming the table you need is the first one

# View the first few rows of the data
print(df.head())

pdb.set_trace()

# Save the DataFrame to a CSV file
# df.to_csv('player_data.csv', index=False)
