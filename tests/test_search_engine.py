import json
import logging
from app import app


def test_search_profile_on_ig_1():
    response = app.test_client().get('/api/v1/instagram/profile?url=https://www.instagram.com/p/BwjxXeTAitg/') 
    assert response.status_code == 200

    data = json.loads(response.data.decode('utf-8'))
    logging.info(data)
    assert type(data) is dict
    assert data['username'] == 'h_a_n.7'

def test_search_profile_on_ig_2():
    response = app.test_client().get('/api/v1/instagram/profile?url=https://www.instagram.com/p/CyXYPgHPeeT/') 
    assert response.status_code == 200

    data = json.loads(response.data.decode('utf-8'))
    logging.info(data)
    assert type(data) is dict
    assert data['username'] == '01.ring'

def test_search_profile_on_ig_3():
    response = app.test_client().get('/api/v1/instagram/profile?url=https://www.instagram.com/p/CYIRN4bPVKj/') 
    assert response.status_code == 200

    data = json.loads(response.data.decode('utf-8'))
    logging.info(data)
    assert type(data) is dict
    assert data['username'] == 'pita_tofua'


def test_search_profile_on_pixnet():
    response = app.test_client().get('/api/v1/pixnet/profile?url=https://www.pixnet.net/pcard/rolahun/profile/info')
    assert response.status_code == 200

    data = json.loads(response.data.decode('utf-8'))
    logging.info(data)
    assert type(data) is dict
    assert data['ig'] == 'rolahun'
    assert data['email'] == 'rolahun221@gmail.com'

def test_search_media_on_pixnet():
    response = app.test_client().get('/api/v1/pixnet/media?keyword=按摩椅')
    assert response.status_code == 200

    data = json.loads(response.data.decode('utf-8'))
    assert type(data['data']['feeds']) is list
    assert '按摩椅' in data['data']['feeds'][0]['description']

