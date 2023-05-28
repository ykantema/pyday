import pytest
import config


def test_update_qn_name(init_api, create_my_qn):
    init_api.update_qn(create_my_qn['id'], 'name', config.user + "1")


@pytest.mark.parametrize('value', ['1', '2', '3'])
def test_update_qn_with_params(init_api, create_my_qn, value):
    new_name = config.user + value
    init_api.update_qn(create_my_qn['id'], 'name', new_name)
    assert(init_api.get_qn(create_my_qn['id'])['name']==new_name)
