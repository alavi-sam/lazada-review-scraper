import requests
from bs4 import BeautifulSoup
import pandas as pd


def extract_product_id(url):
    base_part = url.split('.html')[0]
    return base_part.split('-')[-2][1:]


def get_total_page_number(product_id):
    request_url = f'https://my.lazada.co.id/pdp/review/getReviewList?itemId={product_id}&pageSize=50&filter=0&sort=0&pageNo=1'
    response = requests.get(request_url).json()
    return response['model']['paging']['totalPages']


def get_reviews(page, product_id):
    request_url = f'https://my.lazada.co.id/pdp/review/getReviewList?itemId={product_id}&pageSize=50&filter=0&sort=0&pageNo={page}'
    response = requests.get(request_url)
    return response.json()


def data_to_df(data_json, df):
    data_dict = {col:[] for col in df.columns}
    all_reviews = data_json['model']['items']
    for review in all_reviews:
        for column in df.columns:
            data_dict[column].append(review[column])
    
    reviews_df = pd.DataFrame.from_dict(data_dict)
    return pd.concat([df, reviews_df])



if __name__ == '__main__':
    df = pd.DataFrame(columns=['buyerName', 'rating', 'reviewContent', 'reviewTime'])
    input_url = input('enter your desired url (enter . for sample url):')
    if input_url == '.':
        url = 'https://www.lazada.co.id/products/celana-cargo-wanita-highwaist-bonnie-cargo-pants-celana-kargo-wanita-i7706390243-s14174328153.html?spm=a2o4j.product-not-exist-m.just4u.1.4c9c268dTctOlL&&search=error&clickTrackInfo=d4d4a5eb-e0bc-48e3-83a0-a479dfd90636__7706390243__6567__hot__327975__0.0__0.2202121913433075__0.34739277__0.0__0.004694291__0.8888394832611084__0________0.0________95000.0__0.5947368421052632__4.581538461538462__650__38500.0__127620%2C255084%2C255127%2C255313%2C328068%2C333604%2C350221%2C350829%2C357502%2C366991%2C380123%2C381309%2C522897%2C524869%2C524875%2C525007%2C525880________3650.16539_955.3631_4560.21196____32745____0.22395138__0.0____________0.0__0.0__0.0'
    else:
        url = input_url
    product_id = extract_product_id(url)
    total_page = get_total_page_number(product_id=product_id)
    for page in range(1, total_page+1):
        review_json = get_reviews(page, product_id)
        df = data_to_df(review_json, df)
        print(f'product id: {product_id}', f'reviews_scraped: {df.shape[0]}', f'page number: {page}')
    df.to_csv(f'{product_id}.csv')
