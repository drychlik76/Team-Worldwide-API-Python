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

class GetHouseBillHouseBillHouseBillCollectionGetRead(object):
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
        'house_bill': 'str',
        'created_date_time': 'datetime',
        'reserved': 'bool'
    }

    attribute_map = {
        'house_bill': 'houseBill',
        'created_date_time': 'createdDateTime',
        'reserved': 'reserved'
    }

    def __init__(self, house_bill=None, created_date_time=None, reserved=None):  # noqa: E501
        """GetHouseBillHouseBillHouseBillCollectionGetRead - a model defined in Swagger"""  # noqa: E501
        self._house_bill = None
        self._created_date_time = None
        self._reserved = None
        self.discriminator = None
        if house_bill is not None:
            self.house_bill = house_bill
        if created_date_time is not None:
            self.created_date_time = created_date_time
        if reserved is not None:
            self.reserved = reserved

    @property
    def house_bill(self):
        """Gets the house_bill of this GetHouseBillHouseBillHouseBillCollectionGetRead.  # noqa: E501


        :return: The house_bill of this GetHouseBillHouseBillHouseBillCollectionGetRead.  # noqa: E501
        :rtype: str
        """
        return self._house_bill

    @house_bill.setter
    def house_bill(self, house_bill):
        """Sets the house_bill of this GetHouseBillHouseBillHouseBillCollectionGetRead.


        :param house_bill: The house_bill of this GetHouseBillHouseBillHouseBillCollectionGetRead.  # noqa: E501
        :type: str
        """

        self._house_bill = house_bill

    @property
    def created_date_time(self):
        """Gets the created_date_time of this GetHouseBillHouseBillHouseBillCollectionGetRead.  # noqa: E501


        :return: The created_date_time of this GetHouseBillHouseBillHouseBillCollectionGetRead.  # noqa: E501
        :rtype: datetime
        """
        return self._created_date_time

    @created_date_time.setter
    def created_date_time(self, created_date_time):
        """Sets the created_date_time of this GetHouseBillHouseBillHouseBillCollectionGetRead.


        :param created_date_time: The created_date_time of this GetHouseBillHouseBillHouseBillCollectionGetRead.  # noqa: E501
        :type: datetime
        """

        self._created_date_time = created_date_time

    @property
    def reserved(self):
        """Gets the reserved of this GetHouseBillHouseBillHouseBillCollectionGetRead.  # noqa: E501


        :return: The reserved of this GetHouseBillHouseBillHouseBillCollectionGetRead.  # noqa: E501
        :rtype: bool
        """
        return self._reserved

    @reserved.setter
    def reserved(self, reserved):
        """Sets the reserved of this GetHouseBillHouseBillHouseBillCollectionGetRead.


        :param reserved: The reserved of this GetHouseBillHouseBillHouseBillCollectionGetRead.  # noqa: E501
        :type: bool
        """

        self._reserved = reserved

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
        if issubclass(GetHouseBillHouseBillHouseBillCollectionGetRead, dict):
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
        if not isinstance(other, GetHouseBillHouseBillHouseBillCollectionGetRead):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
