import swagger_client
from helpers import get_key_cloak_token


def test_tags():
    api = swagger_client.api.get_api.GetApi()  # noqa: E501
    c = api.api_client.configuration
    c.host = 'http://192.168.39.186/hub/'
    c.api_key[
        'Authorization'] = get_key_cloak_token(username="admin", password="Dog8code", host="http://192.168.39.186")
    c.api_key_prefix['Authorization'] = 'Bearer'
    d = api.tags_get()
    pass