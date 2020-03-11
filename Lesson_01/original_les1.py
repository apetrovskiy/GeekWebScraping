import requests
import json
import time

URL = 'https://5ka.ru/api/v2/special_offers/'
headers = {'User-agent':
           'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:73.0) \
               Gecko/20100101 Firefox/73.0',
           }
CAT_URL = 'https://5ka.ru/api/v2/categories/'


def x5ka(url, params):
    result = []
    while url:
        response = requests.get(url, headers=headers, params=params) \
            if params else requests.get(url, headers=headers)
        params = None
        data = response.json()
        result.extend(data.get('results'))
        url = data.get('next')
        time.sleep(1)
    return result


if __name__ == '__main__':
    temp_cat = {'parent_group_code': 'PUI2', 'parent_group_name': 'Бананы'}
    # categories = requests.get(CAT_URL, headers=headers)

    data = x5ka(URL, {'records_per_page': 100})

    with open('products.json', 'w') as file:
        file.write(json.dumps(data))
