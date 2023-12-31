import logging
import requests
import re

def get_pixnet_info(url: str):
    email = []
    ig = []

    logging.debug(f'Invoke the Pixnet post API {url}')
    pixnet_user_profile = requests.get(url=url).text

    info_section_pattern = r'<section class="profile-info__intro">(.*?)<\/section>'
    info_section = re.findall(info_section_pattern, pixnet_user_profile, flags=re.MULTILINE|re.DOTALL)

    if len(info_section) == 1: 
        email_pattern = r"[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?" 
        email = re.findall(email_pattern, info_section[0], flags=re.MULTILINE|re.DOTALL)

        ig_pattern = r'instagram\.com[(?:%2F)|\/]([\w](?!.*?\.{2})[\w.]{1,28}[\w])'
        ig = re.findall(ig_pattern, info_section[0], flags=re.MULTILINE|re.DOTALL)
    elif len(info_section) == 0:
        msg = 'No Pixnet info section is found.'
        logging.error(msg)
    else:
        msg = f'Found {len(info_section)} Pixnet info sections.'
        logging.error(msg)
    
    return {
        'email': email[0] if len(email)==1 else '',
        'ig': ig[0] if len(ig)==1 else '',
    }

def get_pixnet_media(keyword: str, page: int):
    url = f'https://www.pixnet.net/mainpage/api/ppage/{keyword}/feeds?page={page}&per_page=25&filter=articles&sort=related'
    logging.debug(f'Invoke the Pixnet post API {url}')
    response = requests.get(url=url)
    
    try:
        response.json()
    except ValueError as err:
        msg = 'Insufficient information, unable to search.'
        logging.error(msg)
        return requests.codes.bad
    return response.json()


if __name__ == '__main__':
    print(get_pixnet_info('https://www.pixnet.net/pcard/rolahun/profile/info'))
