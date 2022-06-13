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


class ApiCopyRequest(object):
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
        'source_review': 'int',
        'target_applications': 'list[int]'
    }

    attribute_map = {
        'source_review': 'sourceReview',
        'target_applications': 'targetApplications'
    }

    def __init__(self, source_review=None, target_applications=None, _configuration=None):  # noqa: E501
        """ApiCopyRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._source_review = None
        self._target_applications = None
        self.discriminator = None

        self.source_review = source_review
        self.target_applications = target_applications

    @property
    def source_review(self):
        """Gets the source_review of this ApiCopyRequest.  # noqa: E501


        :return: The source_review of this ApiCopyRequest.  # noqa: E501
        :rtype: int
        """
        return self._source_review

    @source_review.setter
    def source_review(self, source_review):
        """Sets the source_review of this ApiCopyRequest.


        :param source_review: The source_review of this ApiCopyRequest.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and source_review is None:
            raise ValueError("Invalid value for `source_review`, must not be `None`")  # noqa: E501

        self._source_review = source_review

    @property
    def target_applications(self):
        """Gets the target_applications of this ApiCopyRequest.  # noqa: E501


        :return: The target_applications of this ApiCopyRequest.  # noqa: E501
        :rtype: list[int]
        """
        return self._target_applications

    @target_applications.setter
    def target_applications(self, target_applications):
        """Sets the target_applications of this ApiCopyRequest.


        :param target_applications: The target_applications of this ApiCopyRequest.  # noqa: E501
        :type: list[int]
        """
        if self._configuration.client_side_validation and target_applications is None:
            raise ValueError("Invalid value for `target_applications`, must not be `None`")  # noqa: E501

        self._target_applications = target_applications

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
        if issubclass(ApiCopyRequest, dict):
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
        if not isinstance(other, ApiCopyRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ApiCopyRequest):
            return True

        return self.to_dict() != other.to_dict()
