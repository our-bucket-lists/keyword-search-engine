import logging
import requests
import re

def get_ig_info(url: str):
    username = []

    logging.debug(f'Invoke the IG post API {url}')
    response = requests.get(url=url).text

    username_pattern = r'"description".*?content=".*?([\w_\.]+) on (?:January|February|March|April|May|June|July|August|September|October|November|December)'
    username = re.findall(username_pattern, response, flags=re.MULTILINE|re.DOTALL)

    if len(username) == 1: 
        return {'username': username[0]}
    elif len(username) == 0:
        msg = 'No IG username is found.'
        logging.error(msg)
    else:
        msg = f'Found {len(username)} IG usernames.'
        logging.error(msg)
    

if __name__ == '__main__':
    print(get_ig_info('https://www.instagram.com/p/BwjxXeTAitg/'))
