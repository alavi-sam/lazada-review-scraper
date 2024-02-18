import requests
from bs4 import BeautifulSoup


def extract_product_id(url):
    base_part = url.split('.html')[0]
    return base_part.split('-')[-2][1:]


def get_total_page_number(product_id):
    request_url = f'https://my.lazada.co.id/pdp/review/getReviewList?itemId={product_id}&pageSize=5&filter=0&sort=0&pageNo=1'
    response = requests.get(request_url).json()
    return response['model']['paging']['totalPages']

def get_reviews(page, product_id):
    request_url = f'https://my.lazada.co.id/pdp/review/getReviewList?itemId={product_id}&pageSize=5&filter=0&sort=0&pageNo={page}'
    response = requests.get(request_url)
    return response.json()
