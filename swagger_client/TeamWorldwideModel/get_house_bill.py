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

class GetHouseBill(object):
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
        'branch_id': 'str',
        'account_number': 'str',
        '_class': 'str'
    }

    attribute_map = {
        'branch_id': 'branchId',
        'account_number': 'accountNumber',
        '_class': 'class'
    }

    def __init__(self, branch_id=None, account_number=None, _class=None):  # noqa: E501
        """GetHouseBill - a model defined in Swagger"""  # noqa: E501
        self._branch_id = None
        self._account_number = None
        self.__class = None
        self.discriminator = None
        self.branch_id = branch_id
        if account_number is not None:
            self.account_number = account_number
        if _class is not None:
            self._class = _class

    @property
    def branch_id(self):
        """Gets the branch_id of this GetHouseBill.  # noqa: E501

        Branch ID, or can use Airport code.  This is sometimes referred to as `station id`.  # noqa: E501

        :return: The branch_id of this GetHouseBill.  # noqa: E501
        :rtype: str
        """
        return self._branch_id

    @branch_id.setter
    def branch_id(self, branch_id):
        """Sets the branch_id of this GetHouseBill.

        Branch ID, or can use Airport code.  This is sometimes referred to as `station id`.  # noqa: E501

        :param branch_id: The branch_id of this GetHouseBill.  # noqa: E501
        :type: str
        """
        if branch_id is None:
            raise ValueError("Invalid value for `branch_id`, must not be `None`")  # noqa: E501

        self._branch_id = branch_id

    @property
    def account_number(self):
        """Gets the account_number of this GetHouseBill.  # noqa: E501

        Account number for customer  # noqa: E501

        :return: The account_number of this GetHouseBill.  # noqa: E501
        :rtype: str
        """
        return self._account_number

    @account_number.setter
    def account_number(self, account_number):
        """Sets the account_number of this GetHouseBill.

        Account number for customer  # noqa: E501

        :param account_number: The account_number of this GetHouseBill.  # noqa: E501
        :type: str
        """

        self._account_number = account_number

    @property
    def _class(self):
        """Gets the _class of this GetHouseBill.  # noqa: E501

        Class of house bills          AIR,          AIRT,          CAN,          OCN,          OCNT,          PRIM,          TEST,          TRAC,          TRK,          TRKT        # noqa: E501

        :return: The _class of this GetHouseBill.  # noqa: E501
        :rtype: str
        """
        return self.__class

    @_class.setter
    def _class(self, _class):
        """Sets the _class of this GetHouseBill.

        Class of house bills          AIR,          AIRT,          CAN,          OCN,          OCNT,          PRIM,          TEST,          TRAC,          TRK,          TRKT        # noqa: E501

        :param _class: The _class of this GetHouseBill.  # noqa: E501
        :type: str
        """

        self.__class = _class

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
        if issubclass(GetHouseBill, dict):
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
        if not isinstance(other, GetHouseBill):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
