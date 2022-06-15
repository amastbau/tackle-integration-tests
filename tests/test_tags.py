import logging

import swagger_client
import os

from helpers import get_key_cloak_token


def test_default_tags():
    api = swagger_client.api.get_api.GetApi()  # noqa: E501
    c = api.api_client.configuration
    c.host = f"{os.environ.get('TACKLE_URL')}/hub/"
    c.api_key[
        'Authorization'] = get_key_cloak_token(username=os.environ.get("TACKLE_USER"), password=os.environ.get("TACKLE_PASSWORD"), host=os.environ.get("TACKLE_URL"))  # noqa: E501
    c.api_key_prefix['Authorization'] = 'Bearer'
    assert [tag.name for tag in api.tags_get()] == ['COTS', 'In house', 'SaaS', 'Boston (USA)', 'London (UK)', 'Paris (FR)', 'Sydney (AU)', 'DB2', 'MongoDB', 'Oracle',
     'PostgreSQL', 'SQL Server', 'C# ASP .Net', 'C++', 'COBOL', 'Java', 'Javascript', 'Python', 'RHEL 8',
     'Windows Server 2016', 'Z/OS', 'EAP', 'JWS', 'Quarkus', 'Spring Boot', 'Tomcat', 'WebLogic', 'WebSphere'], "Tags list check failed!" # noqa: E501
