import json

import requests as requests


def get_key_cloak_token(host, username, password, client_id='tackle-ui', realm='tackle'):
    # print("Getting auth token from %s" % host)
    url  = "%s/auth/realms/%s/protocol/openid-connect/token" % (host, realm)
    data = {'username': username, 'password': password, 'client_id': client_id, 'grant_type': 'password'}

    r = requests.post(url, data=data, verify=False)
    if r.ok:
        resp_data = json.loads(r.text)
        return f"Bearer {resp_data['access_token']}"
    else:
        print("ERROR getting auth token from %s" % url)
        print(data, r)
        exit(1)