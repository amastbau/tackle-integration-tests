import argparse
import json

import requests as requests

parser = argparse.ArgumentParser(description='Konveyor Tackle maintenance tool.')
parser.add_argument('-u','--user', dest='user', type=str, help='username')
parser.add_argument('-p','--password', dest='password',type=str, help='password')
parser.add_argument('-l','--host', dest='host',  type=str, help='host')
args = parser.parse_args()


def getKeycloakToken(host, username, password, client_id='tackle-ui', realm='tackle'):
    print("Getting auth token from %s" % host)
    url  = "%s/auth/realms/%s/protocol/openid-connect/token" % (host, realm)
    data = {'username': username, 'password': password, 'client_id': client_id, 'grant_type': 'password'}

    r = requests.post(url, data=data, verify=False)
    if r.ok:
        respData = json.loads(r.text)
        return respData['access_token']
    else:
        print("ERROR getting auth token from %s" % url)
        print(data, r)
        exit(1)


if __name__ == "__main__":
    print(getKeycloakToken(host=args.host, username=args.user, password=args.password))