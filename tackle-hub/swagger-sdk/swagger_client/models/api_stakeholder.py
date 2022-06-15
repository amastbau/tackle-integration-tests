# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class ApiStakeholder(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'business_services': 'list[ApiRef]',
        'create_time': 'str',
        'create_user': 'str',
        'email': 'str',
        'id': 'int',
        'job_function': 'ApiRef',
        'name': 'str',
        'stakeholder_groups': 'list[ApiRef]',
        'update_user': 'str'
    }

    attribute_map = {
        'business_services': 'businessServices',
        'create_time': 'createTime',
        'create_user': 'createUser',
        'email': 'email',
        'id': 'id',
        'job_function': 'jobFunction',
        'name': 'name',
        'stakeholder_groups': 'stakeholderGroups',
        'update_user': 'updateUser'
    }

    def __init__(self, business_services=None, create_time=None, create_user=None, email=None, id=None, job_function=None, name=None, stakeholder_groups=None, update_user=None, _configuration=None):  # noqa: E501
        """ApiStakeholder - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._business_services = None
        self._create_time = None
        self._create_user = None
        self._email = None
        self._id = None
        self._job_function = None
        self._name = None
        self._stakeholder_groups = None
        self._update_user = None
        self.discriminator = None

        if business_services is not None:
            self.business_services = business_services
        if create_time is not None:
            self.create_time = create_time
        if create_user is not None:
            self.create_user = create_user
        self.email = email
        if id is not None:
            self.id = id
        if job_function is not None:
            self.job_function = job_function
        self.name = name
        if stakeholder_groups is not None:
            self.stakeholder_groups = stakeholder_groups
        if update_user is not None:
            self.update_user = update_user

    @property
    def business_services(self):
        """Gets the business_services of this ApiStakeholder.  # noqa: E501


        :return: The business_services of this ApiStakeholder.  # noqa: E501
        :rtype: list[ApiRef]
        """
        return self._business_services

    @business_services.setter
    def business_services(self, business_services):
        """Sets the business_services of this ApiStakeholder.


        :param business_services: The business_services of this ApiStakeholder.  # noqa: E501
        :type: list[ApiRef]
        """

        self._business_services = business_services

    @property
    def create_time(self):
        """Gets the create_time of this ApiStakeholder.  # noqa: E501


        :return: The create_time of this ApiStakeholder.  # noqa: E501
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ApiStakeholder.


        :param create_time: The create_time of this ApiStakeholder.  # noqa: E501
        :type: str
        """

        self._create_time = create_time

    @property
    def create_user(self):
        """Gets the create_user of this ApiStakeholder.  # noqa: E501


        :return: The create_user of this ApiStakeholder.  # noqa: E501
        :rtype: str
        """
        return self._create_user

    @create_user.setter
    def create_user(self, create_user):
        """Sets the create_user of this ApiStakeholder.


        :param create_user: The create_user of this ApiStakeholder.  # noqa: E501
        :type: str
        """

        self._create_user = create_user

    @property
    def email(self):
        """Gets the email of this ApiStakeholder.  # noqa: E501


        :return: The email of this ApiStakeholder.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this ApiStakeholder.


        :param email: The email of this ApiStakeholder.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def id(self):
        """Gets the id of this ApiStakeholder.  # noqa: E501


        :return: The id of this ApiStakeholder.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ApiStakeholder.


        :param id: The id of this ApiStakeholder.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def job_function(self):
        """Gets the job_function of this ApiStakeholder.  # noqa: E501


        :return: The job_function of this ApiStakeholder.  # noqa: E501
        :rtype: ApiRef
        """
        return self._job_function

    @job_function.setter
    def job_function(self, job_function):
        """Sets the job_function of this ApiStakeholder.


        :param job_function: The job_function of this ApiStakeholder.  # noqa: E501
        :type: ApiRef
        """

        self._job_function = job_function

    @property
    def name(self):
        """Gets the name of this ApiStakeholder.  # noqa: E501


        :return: The name of this ApiStakeholder.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ApiStakeholder.


        :param name: The name of this ApiStakeholder.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def stakeholder_groups(self):
        """Gets the stakeholder_groups of this ApiStakeholder.  # noqa: E501


        :return: The stakeholder_groups of this ApiStakeholder.  # noqa: E501
        :rtype: list[ApiRef]
        """
        return self._stakeholder_groups

    @stakeholder_groups.setter
    def stakeholder_groups(self, stakeholder_groups):
        """Sets the stakeholder_groups of this ApiStakeholder.


        :param stakeholder_groups: The stakeholder_groups of this ApiStakeholder.  # noqa: E501
        :type: list[ApiRef]
        """

        self._stakeholder_groups = stakeholder_groups

    @property
    def update_user(self):
        """Gets the update_user of this ApiStakeholder.  # noqa: E501


        :return: The update_user of this ApiStakeholder.  # noqa: E501
        :rtype: str
        """
        return self._update_user

    @update_user.setter
    def update_user(self, update_user):
        """Sets the update_user of this ApiStakeholder.


        :param update_user: The update_user of this ApiStakeholder.  # noqa: E501
        :type: str
        """

        self._update_user = update_user

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(ApiStakeholder, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ApiStakeholder):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ApiStakeholder):
            return True

        return self.to_dict() != other.to_dict()