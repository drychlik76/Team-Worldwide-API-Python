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

class GetQuoteQuoteResponse(object):
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
        'unique_id': 'str',
        'quote_id': 'int',
        'quote_number': 'str',
        'house_bill': 'str'
    }

    attribute_map = {
        'unique_id': 'uniqueId',
        'quote_id': 'quoteId',
        'quote_number': 'quoteNumber',
        'house_bill': 'houseBill'
    }

    def __init__(self, unique_id=None, quote_id=None, quote_number=None, house_bill=None):  # noqa: E501
        """GetQuoteQuoteResponse - a model defined in Swagger"""  # noqa: E501
        self._unique_id = None
        self._quote_id = None
        self._quote_number = None
        self._house_bill = None
        self.discriminator = None
        if unique_id is not None:
            self.unique_id = unique_id
        if quote_id is not None:
            self.quote_id = quote_id
        if quote_number is not None:
            self.quote_number = quote_number
        if house_bill is not None:
            self.house_bill = house_bill

    @property
    def unique_id(self):
        """Gets the unique_id of this GetQuoteQuoteResponse.  # noqa: E501


        :return: The unique_id of this GetQuoteQuoteResponse.  # noqa: E501
        :rtype: str
        """
        return self._unique_id

    @unique_id.setter
    def unique_id(self, unique_id):
        """Sets the unique_id of this GetQuoteQuoteResponse.


        :param unique_id: The unique_id of this GetQuoteQuoteResponse.  # noqa: E501
        :type: str
        """

        self._unique_id = unique_id

    @property
    def quote_id(self):
        """Gets the quote_id of this GetQuoteQuoteResponse.  # noqa: E501


        :return: The quote_id of this GetQuoteQuoteResponse.  # noqa: E501
        :rtype: int
        """
        return self._quote_id

    @quote_id.setter
    def quote_id(self, quote_id):
        """Sets the quote_id of this GetQuoteQuoteResponse.


        :param quote_id: The quote_id of this GetQuoteQuoteResponse.  # noqa: E501
        :type: int
        """

        self._quote_id = quote_id

    @property
    def quote_number(self):
        """Gets the quote_number of this GetQuoteQuoteResponse.  # noqa: E501


        :return: The quote_number of this GetQuoteQuoteResponse.  # noqa: E501
        :rtype: str
        """
        return self._quote_number

    @quote_number.setter
    def quote_number(self, quote_number):
        """Sets the quote_number of this GetQuoteQuoteResponse.


        :param quote_number: The quote_number of this GetQuoteQuoteResponse.  # noqa: E501
        :type: str
        """

        self._quote_number = quote_number

    @property
    def house_bill(self):
        """Gets the house_bill of this GetQuoteQuoteResponse.  # noqa: E501


        :return: The house_bill of this GetQuoteQuoteResponse.  # noqa: E501
        :rtype: str
        """
        return self._house_bill

    @house_bill.setter
    def house_bill(self, house_bill):
        """Sets the house_bill of this GetQuoteQuoteResponse.


        :param house_bill: The house_bill of this GetQuoteQuoteResponse.  # noqa: E501
        :type: str
        """

        self._house_bill = house_bill

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
        if issubclass(GetQuoteQuoteResponse, dict):
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
        if not isinstance(other, GetQuoteQuoteResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
