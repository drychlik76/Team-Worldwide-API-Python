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

class BookShipmentTeamBookResponse(object):
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
        'bol_number': 'str',
        'bol_prefix': 'str',
        'accessorials': 'list[str]',
        'dispatched': 'bool',
        'dispatch_error': 'str',
        'total_weight': 'float',
        'b_ol_number': 'str',
        'b_ol_prefix': 'str'
    }

    attribute_map = {
        'house_bill': 'houseBill',
        'bol_number': 'BOLNumber',
        'bol_prefix': 'BOLPrefix',
        'accessorials': 'accessorials',
        'dispatched': 'dispatched',
        'dispatch_error': 'dispatchError',
        'total_weight': 'totalWeight',
        'b_ol_number': 'bOLNumber',
        'b_ol_prefix': 'bOLPrefix'
    }

    def __init__(self, house_bill=None, bol_number=None, bol_prefix=None, accessorials=None, dispatched=None, dispatch_error=None, total_weight=None, b_ol_number=None, b_ol_prefix=None):  # noqa: E501
        """BookShipmentTeamBookResponse - a model defined in Swagger"""  # noqa: E501
        self._house_bill = None
        self._bol_number = None
        self._bol_prefix = None
        self._accessorials = None
        self._dispatched = None
        self._dispatch_error = None
        self._total_weight = None
        self._b_ol_number = None
        self._b_ol_prefix = None
        self.discriminator = None
        if house_bill is not None:
            self.house_bill = house_bill
        if bol_number is not None:
            self.bol_number = bol_number
        if bol_prefix is not None:
            self.bol_prefix = bol_prefix
        if accessorials is not None:
            self.accessorials = accessorials
        if dispatched is not None:
            self.dispatched = dispatched
        if dispatch_error is not None:
            self.dispatch_error = dispatch_error
        if total_weight is not None:
            self.total_weight = total_weight
        if b_ol_number is not None:
            self.b_ol_number = b_ol_number
        if b_ol_prefix is not None:
            self.b_ol_prefix = b_ol_prefix

    @property
    def house_bill(self):
        """Gets the house_bill of this BookShipmentTeamBookResponse.  # noqa: E501


        :return: The house_bill of this BookShipmentTeamBookResponse.  # noqa: E501
        :rtype: str
        """
        return self._house_bill

    @house_bill.setter
    def house_bill(self, house_bill):
        """Sets the house_bill of this BookShipmentTeamBookResponse.


        :param house_bill: The house_bill of this BookShipmentTeamBookResponse.  # noqa: E501
        :type: str
        """

        self._house_bill = house_bill

    @property
    def bol_number(self):
        """Gets the bol_number of this BookShipmentTeamBookResponse.  # noqa: E501


        :return: The bol_number of this BookShipmentTeamBookResponse.  # noqa: E501
        :rtype: str
        """
        return self._bol_number

    @bol_number.setter
    def bol_number(self, bol_number):
        """Sets the bol_number of this BookShipmentTeamBookResponse.


        :param bol_number: The bol_number of this BookShipmentTeamBookResponse.  # noqa: E501
        :type: str
        """

        self._bol_number = bol_number

    @property
    def bol_prefix(self):
        """Gets the bol_prefix of this BookShipmentTeamBookResponse.  # noqa: E501


        :return: The bol_prefix of this BookShipmentTeamBookResponse.  # noqa: E501
        :rtype: str
        """
        return self._bol_prefix

    @bol_prefix.setter
    def bol_prefix(self, bol_prefix):
        """Sets the bol_prefix of this BookShipmentTeamBookResponse.


        :param bol_prefix: The bol_prefix of this BookShipmentTeamBookResponse.  # noqa: E501
        :type: str
        """

        self._bol_prefix = bol_prefix

    @property
    def accessorials(self):
        """Gets the accessorials of this BookShipmentTeamBookResponse.  # noqa: E501


        :return: The accessorials of this BookShipmentTeamBookResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._accessorials

    @accessorials.setter
    def accessorials(self, accessorials):
        """Sets the accessorials of this BookShipmentTeamBookResponse.


        :param accessorials: The accessorials of this BookShipmentTeamBookResponse.  # noqa: E501
        :type: list[str]
        """

        self._accessorials = accessorials

    @property
    def dispatched(self):
        """Gets the dispatched of this BookShipmentTeamBookResponse.  # noqa: E501


        :return: The dispatched of this BookShipmentTeamBookResponse.  # noqa: E501
        :rtype: bool
        """
        return self._dispatched

    @dispatched.setter
    def dispatched(self, dispatched):
        """Sets the dispatched of this BookShipmentTeamBookResponse.


        :param dispatched: The dispatched of this BookShipmentTeamBookResponse.  # noqa: E501
        :type: bool
        """

        self._dispatched = dispatched

    @property
    def dispatch_error(self):
        """Gets the dispatch_error of this BookShipmentTeamBookResponse.  # noqa: E501


        :return: The dispatch_error of this BookShipmentTeamBookResponse.  # noqa: E501
        :rtype: str
        """
        return self._dispatch_error

    @dispatch_error.setter
    def dispatch_error(self, dispatch_error):
        """Sets the dispatch_error of this BookShipmentTeamBookResponse.


        :param dispatch_error: The dispatch_error of this BookShipmentTeamBookResponse.  # noqa: E501
        :type: str
        """

        self._dispatch_error = dispatch_error

    @property
    def total_weight(self):
        """Gets the total_weight of this BookShipmentTeamBookResponse.  # noqa: E501


        :return: The total_weight of this BookShipmentTeamBookResponse.  # noqa: E501
        :rtype: float
        """
        return self._total_weight

    @total_weight.setter
    def total_weight(self, total_weight):
        """Sets the total_weight of this BookShipmentTeamBookResponse.


        :param total_weight: The total_weight of this BookShipmentTeamBookResponse.  # noqa: E501
        :type: float
        """

        self._total_weight = total_weight

    @property
    def b_ol_number(self):
        """Gets the b_ol_number of this BookShipmentTeamBookResponse.  # noqa: E501


        :return: The b_ol_number of this BookShipmentTeamBookResponse.  # noqa: E501
        :rtype: str
        """
        return self._b_ol_number

    @b_ol_number.setter
    def b_ol_number(self, b_ol_number):
        """Sets the b_ol_number of this BookShipmentTeamBookResponse.


        :param b_ol_number: The b_ol_number of this BookShipmentTeamBookResponse.  # noqa: E501
        :type: str
        """

        self._b_ol_number = b_ol_number

    @property
    def b_ol_prefix(self):
        """Gets the b_ol_prefix of this BookShipmentTeamBookResponse.  # noqa: E501


        :return: The b_ol_prefix of this BookShipmentTeamBookResponse.  # noqa: E501
        :rtype: str
        """
        return self._b_ol_prefix

    @b_ol_prefix.setter
    def b_ol_prefix(self, b_ol_prefix):
        """Sets the b_ol_prefix of this BookShipmentTeamBookResponse.


        :param b_ol_prefix: The b_ol_prefix of this BookShipmentTeamBookResponse.  # noqa: E501
        :type: str
        """

        self._b_ol_prefix = b_ol_prefix

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
        if issubclass(BookShipmentTeamBookResponse, dict):
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
        if not isinstance(other, BookShipmentTeamBookResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
