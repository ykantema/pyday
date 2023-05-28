import pytest
import config
from api import API


@pytest.fixture(scope='session')
def init_api():
    api = API()
    api.login()
    print('login')
    return api


@pytest.fixture(scope='function')
def create_my_qn(init_api):
    qns = init_api.get_qns()
    for qn in qns['entities']:
        if config.user in qn['name']:
            print('found qn name {} as {}'.format(config.user, qn))
            return qn
    res = init_api.create_qn(config.user)
    print('create new qn {}'.format(res))
    return res


@pytest.fixture(scope='session', autouse=True)
def clean_my_qns(init_api):
    yield
    print("clean all")
    qns = init_api.get_qns()
    for qn in qns['entities']:
        if config.user in qn['name']:
            print('found qn name {} as {}'.format(config.user, qn))
            init_api.delete_qn(qn['id'])

