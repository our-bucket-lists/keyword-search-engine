from flask import jsonify
import requests
import logging
import re

def get_ig_info(url: str):
    username = []
    fullname = []

    logging.debug(f'Invoke the IG post API {url}')
    response = requests.get(url=url).text

    username_pattern = r'"description".*?content=".*?likes,.*?comments - ([\w_\.]+).*?on (?:January|February|March|April|May|June|July|August|September|October|November|December)'
    username = re.findall(username_pattern, response, flags=re.MULTILINE|re.DOTALL)

    if len(username) == 1: 
        logging.debug(f'Invoke the IG user profile API {url}')
        response = requests.get(f'https://www.instagram.com/{username[0]}').text

        fullname_pattern = r'<title>(.*?)\s\(&#064;.*?\).*<\/title>'
        fullname = re.findall(fullname_pattern, response, flags=re.MULTILINE|re.DOTALL)
    elif len(username) == 0:
        msg = 'No IG username is found.'
        logging.error(msg)
    else:
        msg = f'Found {len(username)} IG usernames.'
        logging.error(msg)
    
    return {
        'username': username[0] if len(username)==1 else '',
        'fullname': fullname[0] if len(fullname)==1 else '',
    }

if __name__ == '__main__':
    print(get_ig_info('https://www.instagram.com/p/BwjxXeTAitg/'))
