import json
import logging
from app import app


def test_search_on_ig():
    response = app.test_client().get('/api/v1/instagram?url=https://www.instagram.com/p/BwjxXeTAitg/') 
    assert response.status_code == 200

    data = json.loads(response.data.decode('utf-8'))
    logging.info(data)
    assert type(data) is dict
    assert data['username'] == 'h_a_n.7'
    assert data['fullname'] == 'Sammy山米 ✌︎ 台中 台北 美食·小吃·旅遊·親子·育兒'


def test_search_on_pixnet():
    response = app.test_client().get('/api/v1/pixnet?url=https://www.pixnet.net/pcard/rolahun/profile/info')
    assert response.status_code == 200

    data = json.loads(response.data.decode('utf-8'))
    logging.info(data)
    assert type(data) is dict
    assert data['ig'] == 'rolahun'
    assert data['email'] == 'rolahun221@gmail.com'

