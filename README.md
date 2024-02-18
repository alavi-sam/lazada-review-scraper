# Lazada Review Scraper

This Python script is designed to scrape reviews for specific products on Lazada's website. It automates the collection of product reviews and compiles them into a CSV file for further analysis or review.

## Features

- Extracts product ID from the provided product URL.
- Fetches total number of pages of reviews for a product.
- Collects reviews from each page.
- Compiles review data into a pandas DataFrame and exports it to a CSV file.

## Prerequisites

Before running the script, ensure you have Python installed on your system along with the following packages:

- requests
- BeautifulSoup4 (bs4)
- pandas

You can install these packages using pip:

```
pip install requests beautifulsoup4 pandas
```

## How to Use

1. **Start the Script**: Run the script in your terminal or command prompt.

```bash
python lazada_review_scraper.py
```

2. **Enter the Product URL**: When prompted, input the URL of the product you wish to scrape reviews for. If you want to use a sample URL provided in the script, simply enter `.`.

3. **Review Collection**: The script will automatically start collecting reviews from the product page, across all review pages. Progress will be printed in the terminal, showing the product ID, number of reviews scraped, and the current page number.

4. **CSV Output**: Once complete, the script outputs a CSV file named after the product ID, containing all the scraped reviews.

## Functions Explained

- `extract_product_id(url)`: Extracts the product ID from the given product URL.

- `get_total_page_number(product_id)`: Fetches the total number of pages of reviews for the product, using its ID.

- `get_reviews(page, product_id)`: Retrieves the review data in JSON format for a specific page and product ID.

- `data_to_df(data_json, df)`: Converts the JSON data of reviews into a pandas DataFrame and appends it to the existing DataFrame. This function is used iteratively to compile reviews from all pages.

## Notes

- The script uses a sample URL for demonstration purposes. Replace it with the desired product URL or input it when prompted.
- Ensure your internet connection is stable while running the script to avoid any interruptions during the data scraping process.

## Disclaimer

This script is for educational purposes only. Please be mindful of Lazada's terms of service regarding web scraping and use this script responsibly.
