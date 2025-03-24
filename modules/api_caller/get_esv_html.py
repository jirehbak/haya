import sys
import requests


API_KEY = 'fd4c2adece7d4342672bc77d5b846cbb2cf2fd74'
API_URL = 'https://api.esv.org/v3/passage/html/'


def get_esv_html(passage):
    params = {
        'q': passage,
        'include-headings': False,
        # 'include-footnotes': False,
        # 'include-verse-numbers': False,
        # 'include-short-copyright': False,
        # 'include-passage-references': False
    }

    headers = {
        'Authorization': 'Token %s' % API_KEY
    }

    response = requests.get(API_URL, params=params, headers=headers)

    passages = response.json()['passages']

    return passages[0].strip() if passages else 'Error: Passage not found'


if __name__ == '__main__':
    passage = ' '.join(sys.argv[1:])

    if passage:
        print(get_esv_html(passage))