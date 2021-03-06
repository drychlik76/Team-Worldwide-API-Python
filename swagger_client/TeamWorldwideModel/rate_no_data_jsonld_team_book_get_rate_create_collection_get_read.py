# coding: utf-8

"""
    Team Worldwide API 2022

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.0.5
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class RateNoDataJsonldTeamBookGetRateCreateCollectionGetRead(object):
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
        'context': 'OneOfRateNoDataJsonldTeamBookGetRateCreateCollectionGetReadContext',
        'id': 'str',
        'type': 'str',
        'vendor': 'str',
        'response': 'str'
    }

    attribute_map = {
        'context': '@context',
        'id': '@id',
        'type': '@type',
        'vendor': 'vendor',
        'response': 'response'
    }

    def __init__(self, context=None, id=None, type=None, vendor=None, response=None):  # noqa: E501
        """RateNoDataJsonldTeamBookGetRateCreateCollectionGetRead - a model defined in Swagger"""  # noqa: E501
        self._context = None
        self._id = None
        self._type = None
        self._vendor = None
        self._response = None
        self.discriminator = None
        if context is not None:
            self.context = context
        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if vendor is not None:
            self.vendor = vendor
        if response is not None:
            self.response = response

    @property
    def context(self):
        """Gets the context of this RateNoDataJsonldTeamBookGetRateCreateCollectionGetRead.  # noqa: E501


        :return: The context of this RateNoDataJsonldTeamBookGetRateCreateCollectionGetRead.  # noqa: E501
        :rtype: OneOfRateNoDataJsonldTeamBookGetRateCreateCollectionGetReadContext
        """
        return self._context

    @context.setter
    def context(self, context):
        """Sets the context of this RateNoDataJsonldTeamBookGetRateCreateCollectionGetRead.


        :param context: The context of this RateNoDataJsonldTeamBookGetRateCreateCollectionGetRead.  # noqa: E501
        :type: OneOfRateNoDataJsonldTeamBookGetRateCreateCollectionGetReadContext
        """

        self._context = context

    @property
    def id(self):
        """Gets the id of this RateNoDataJsonldTeamBookGetRateCreateCollectionGetRead.  # noqa: E501


        :return: The id of this RateNoDataJsonldTeamBookGetRateCreateCollectionGetRead.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RateNoDataJsonldTeamBookGetRateCreateCollectionGetRead.


        :param id: The id of this RateNoDataJsonldTeamBookGetRateCreateCollectionGetRead.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this RateNoDataJsonldTeamBookGetRateCreateCollectionGetRead.  # noqa: E501


        :return: The type of this RateNoDataJsonldTeamBookGetRateCreateCollectionGetRead.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this RateNoDataJsonldTeamBookGetRateCreateCollectionGetRead.


        :param type: The type of this RateNoDataJsonldTeamBookGetRateCreateCollectionGetRead.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def vendor(self):
        """Gets the vendor of this RateNoDataJsonldTeamBookGetRateCreateCollectionGetRead.  # noqa: E501


        :return: The vendor of this RateNoDataJsonldTeamBookGetRateCreateCollectionGetRead.  # noqa: E501
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        """Sets the vendor of this RateNoDataJsonldTeamBookGetRateCreateCollectionGetRead.


        :param vendor: The vendor of this RateNoDataJsonldTeamBookGetRateCreateCollectionGetRead.  # noqa: E501
        :type: str
        """

        self._vendor = vendor

    @property
    def response(self):
        """Gets the response of this RateNoDataJsonldTeamBookGetRateCreateCollectionGetRead.  # noqa: E501


        :return: The response of this RateNoDataJsonldTeamBookGetRateCreateCollectionGetRead.  # noqa: E501
        :rtype: str
        """
        return self._response

    @response.setter
    def response(self, response):
        """Sets the response of this RateNoDataJsonldTeamBookGetRateCreateCollectionGetRead.


        :param response: The response of this RateNoDataJsonldTeamBookGetRateCreateCollectionGetRead.  # noqa: E501
        :type: str
        """

        self._response = response

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
        if issubclass(RateNoDataJsonldTeamBookGetRateCreateCollectionGetRead, dict):
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
        if not isinstance(other, RateNoDataJsonldTeamBookGetRateCreateCollectionGetRead):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
