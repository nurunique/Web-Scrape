# Flipkart scraping code

# How To Use:
# 1. change url, which you want to srape
# 2.change number how many pages you want to srape
# 3. make sure the path, where you want the xlsx file

# ISSUE:
# There is problem in this code. When You scrape you got three empty rows(1st , 25th, 26th). Because of code consider pages 1st, 25th
# , 26th's as a product. but those are not product , those are just text. 
# So when extract need to fix the empty rows by ms excell tools. 
# need to fix the problem. we are trying fix the problem.

import requests
from bs4 import BeautifulSoup
import pandas as pd

# Create empty list for storing values
names, prices, descriptions, ratings, reviews, links = [], [], [], [], [], []

# Initialized scraping page number
for i in range(1,2):
    url = 'https://www.flipkart.com/search?q=Tv&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=' + str(i)
    #headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}

    response = requests.get(url)
    #response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Find all product containers
    products = soup.find("div", class_="DOjaWF gdgoEp")  # Update the class to match Flipkart's structure

    # Initialize lists for data
    for product in products:
        # Extract the name
        name = product.find("div", class_="KzDlHZ")
        names.append(name.text if name else None)

        # Extract the price
        price = product.find('div', class_="Nx9bqj _4b5DiR")
        prices.append(price.text if name else None)
        
        # Extract the description
        description = product.find("ul", class_="G4BRas")
        descriptions.append(description.text if description else None)
        
        # Extract the rating
        rating = product.find("div", class_="XQDdHH")
        ratings.append(rating.text if rating else None)

        # Extract the reviews
        review = product.find('span', class_='Wphh3N')
        reviews.append(review.text if review else None)
        
        # Extract the Link
        link = product.find('a', class_='CGtC98', href=True)
        links.append(('https://www.flipkart.com' + link['href']) if link else None)

    # Store the Values
    data = {
        "Name": names[1:],
        "Price": prices[1:],
        "Description": descriptions[1:],
        "Ratings": ratings[1:],
        "Reviews": reviews[1:],
        "Links": links[1:]
    }

# Create Dataframe
df = pd.DataFrame(data)

# Save to Excel
df.to_excel("flipkart_productts_all.xlsx", index=False)
print("Data has been successfully scraped and saved to flipkart_products.xlsx")
