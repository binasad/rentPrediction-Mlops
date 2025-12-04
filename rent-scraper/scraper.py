from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import csv

# 1. SETUP THE ROBOT
options = webdriver.ChromeOptions()
# We keep it visible (not headless) for now so you can watch it work!
# HARDCODED PATH to bypass the error
driver_path = r"C:\Users\This PC\.wdm\drivers\chromedriver\win64\142.0.7444.175\chromedriver-win32\chromedriver.exe"

driver = webdriver.Chrome(service=Service(driver_path), options=options)

try:
    print("---------------------------------------")
    print("🤖 Robot starting...")

    # 2. GO TO THE WEBSITE
    # (Using a search page for Islamabad - you can change this URL to any listing page)
    url = "https://www.zameen.com/Homes/Islamabad-3-1.html" 
    print(f"Opening {url}...")
    driver.get(url)
    
    # Wait for the page to load
    time.sleep(5) 

    # 3. FIND DATA
    # We look for the tag 'li' that has the specific label 'Listing'
    cards = driver.find_elements(By.CSS_SELECTOR, 'li[aria-label="Listing"]')
    print(f"Found {len(cards)} listings on this page.")
    
    data_list = []
    
    for card in cards:
        try:
            # YOUR CODE GOES HERE:
            price_text = card.find_element(By.CSS_SELECTOR, '[aria-label="Price"]').text
            # CHANGE "Property header" TO "Location"
            location_text = card.find_element(By.CSS_SELECTOR, '[aria-label="Location"]').text
            area_text = card.find_element(By.CSS_SELECTOR, '[aria-label="Area"]').text
            beds_text = card.find_element(By.CSS_SELECTOR, '[aria-label="Beds"]').text
            
            # Clean and Store
            row = [location_text, area_text, beds_text, price_text]
            data_list.append(row)
            print(f"Scraped: {row}")
            
        except Exception as e:
            print(f"⚠️ Skipping card. Reason: {e}")
            continue

    # 4. SAVE TO CSV
    with open('housing.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Location", "Area", "Beds", "Price"]) # Header
        writer.writerows(data_list)
        
    print(f"Successfully saved {len(data_list)} listings to housing.csv")

except Exception as e:
    print(f"Error: {e}")

finally:
    driver.quit()
    print("---------------------------------------")
    print("🤖 Robot finished.")

def clean_area(area_text):
    if not isinstance(area_text, str): return area_text
    parts = area_text.split() 
    number = float(parts[0])
    unit = parts[1]
    
    if unit == "Kanal":
        return number * 20   # <--- How many Marlas are in a Kanal?
        
    return number # It's already in Marla

def clean_price(price_text):
    # 1. Split the text to get the number and the unit
    # "2.2 Crore" -> parts = ["2.2", "Crore"]
    parts = price_text.split() 
    
    number = float(parts[0]) # This gives us 2.2
    unit = parts[1]          # This gives us "Crore"
    
    # 2. Check the unit and multiply
    if unit == "Crore":
        return number * 10000000 # <--- What goes here?
        
    elif unit == "Lakh":
        return 100000          # <--- And here?
        
    return number # Fallback