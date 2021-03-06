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

class RateDataJsonldTeamBookGetRateCreateCollectionGetRead(object):
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
        'context': 'OneOfRateDataJsonldTeamBookGetRateCreateCollectionGetReadContext',
        'id': 'str',
        'type': 'str',
        'rate_id': 'str',
        'name': 'str',
        'code': 'str',
        'service_level': 'str',
        'account_number': 'str',
        'total': 'float',
        'rate_type': 'str',
        'transit_days': 'int',
        'icon_url': 'str',
        'rate_remarks': 'list[str]',
        'rate_break_down_list': 'list[RateBreakDownJsonldTeamBookGetRateCreateCollectionGetRead]'
    }

    attribute_map = {
        'context': '@context',
        'id': '@id',
        'type': '@type',
        'rate_id': 'rateId',
        'name': 'name',
        'code': 'code',
        'service_level': 'serviceLevel',
        'account_number': 'accountNumber',
        'total': 'total',
        'rate_type': 'rateType',
        'transit_days': 'transitDays',
        'icon_url': 'iconUrl',
        'rate_remarks': 'rateRemarks',
        'rate_break_down_list': 'rateBreakDownList'
    }

    def __init__(self, context=None, id=None, type=None, rate_id=None, name=None, code=None, service_level=None, account_number=None, total=None, rate_type=None, transit_days=None, icon_url=None, rate_remarks=None, rate_break_down_list=None):  # noqa: E501
        """RateDataJsonldTeamBookGetRateCreateCollectionGetRead - a model defined in Swagger"""  # noqa: E501
        self._context = None
        self._id = None
        self._type = None
        self._rate_id = None
        self._name = None
        self._code = None
        self._service_level = None
        self._account_number = None
        self._total = None
        self._rate_type = None
        self._transit_days = None
        self._icon_url = None
        self._rate_remarks = None
        self._rate_break_down_list = None
        self.discriminator = None
        if context is not None:
            self.context = context
        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if rate_id is not None:
            self.rate_id = rate_id
        if name is not None:
            self.name = name
        if code is not None:
            self.code = code
        if service_level is not None:
            self.service_level = service_level
        if account_number is not None:
            self.account_number = account_number
        if total is not None:
            self.total = total
        if rate_type is not None:
            self.rate_type = rate_type
        if transit_days is not None:
            self.transit_days = transit_days
        if icon_url is not None:
            self.icon_url = icon_url
        if rate_remarks is not None:
            self.rate_remarks = rate_remarks
        if rate_break_down_list is not None:
            self.rate_break_down_list = rate_break_down_list

    @property
    def context(self):
        """Gets the context of this RateDataJsonldTeamBookGetRateCreateCollectionGetRead.  # noqa: E501


        :return: The context of this RateDataJsonldTeamBookGetRateCreateCollectionGetRead.  # noqa: E501
        :rtype: OneOfRateDataJsonldTeamBookGetRateCreateCollectionGetReadContext
        """
        return self._context

    @context.setter
    def context(self, context):
        """Sets the context of this RateDataJsonldTeamBookGetRateCreateCollectionGetRead.


        :param context: The context of this RateDataJsonldTeamBookGetRateCreateCollectionGetRead.  # noqa: E501
        :type: OneOfRateDataJsonldTeamBookGetRateCreateCollectionGetReadContext
        """

        self._context = context

    @property
    def id(self):
        """Gets the id of this RateDataJsonldTeamBookGetRateCreateCollectionGetRead.  # noqa: E501


        :return: The id of this RateDataJsonldTeamBookGetRateCreateCollectionGetRead.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RateDataJsonldTeamBookGetRateCreateCollectionGetRead.


        :param id: The id of this RateDataJsonldTeamBookGetRateCreateCollectionGetRead.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this RateDataJsonldTeamBookGetRateCreateCollectionGetRead.  # noqa: E501


        :return: The type of this RateDataJsonldTeamBookGetRateCreateCollectionGetRead.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this RateDataJsonldTeamBookGetRateCreateCollectionGetRead.


        :param type: The type of this RateDataJsonldTeamBookGetRateCreateCollectionGetRead.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def rate_id(self):
        """Gets the rate_id of this RateDataJsonldTeamBookGetRateCreateCollectionGetRead.  # noqa: E501


        :return: The rate_id of this RateDataJsonldTeamBookGetRateCreateCollectionGetRead.  # noqa: E501
        :rtype: str
        """
        return self._rate_id

    @rate_id.setter
    def rate_id(self, rate_id):
        """Sets the rate_id of this RateDataJsonldTeamBookGetRateCreateCollectionGetRead.


        :param rate_id: The rate_id of this RateDataJsonldTeamBookGetRateCreateCollectionGetRead.  # noqa: E501
        :type: str
        """

        self._rate_id = rate_id

    @property
    def name(self):
        """Gets the name of this RateDataJsonldTeamBookGetRateCreateCollectionGetRead.  # noqa: E501


        :return: The name of this RateDataJsonldTeamBookGetRateCreateCollectionGetRead.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RateDataJsonldTeamBookGetRateCreateCollectionGetRead.


        :param name: The name of this RateDataJsonldTeamBookGetRateCreateCollectionGetRead.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def code(self):
        """Gets the code of this RateDataJsonldTeamBookGetRateCreateCollectionGetRead.  # noqa: E501


        :return: The code of this RateDataJsonldTeamBookGetRateCreateCollectionGetRead.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this RateDataJsonldTeamBookGetRateCreateCollectionGetRead.


        :param code: The code of this RateDataJsonldTeamBookGetRateCreateCollectionGetRead.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def service_level(self):
        """Gets the service_level of this RateDataJsonldTeamBookGetRateCreateCollectionGetRead.  # noqa: E501


        :return: The service_level of this RateDataJsonldTeamBookGetRateCreateCollectionGetRead.  # noqa: E501
        :rtype: str
        """
        return self._service_level

    @service_level.setter
    def service_level(self, service_level):
        """Sets the service_level of this RateDataJsonldTeamBookGetRateCreateCollectionGetRead.


        :param service_level: The service_level of this RateDataJsonldTeamBookGetRateCreateCollectionGetRead.  # noqa: E501
        :type: str
        """

        self._service_level = service_level

    @property
    def account_number(self):
        """Gets the account_number of this RateDataJsonldTeamBookGetRateCreateCollectionGetRead.  # noqa: E501


        :return: The account_number of this RateDataJsonldTeamBookGetRateCreateCollectionGetRead.  # noqa: E501
        :rtype: str
        """
        return self._account_number

    @account_number.setter
    def account_number(self, account_number):
        """Sets the account_number of this RateDataJsonldTeamBookGetRateCreateCollectionGetRead.


        :param account_number: The account_number of this RateDataJsonldTeamBookGetRateCreateCollectionGetRead.  # noqa: E501
        :type: str
        """

        self._account_number = account_number

    @property
    def total(self):
        """Gets the total of this RateDataJsonldTeamBookGetRateCreateCollectionGetRead.  # noqa: E501


        :return: The total of this RateDataJsonldTeamBookGetRateCreateCollectionGetRead.  # noqa: E501
        :rtype: float
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this RateDataJsonldTeamBookGetRateCreateCollectionGetRead.


        :param total: The total of this RateDataJsonldTeamBookGetRateCreateCollectionGetRead.  # noqa: E501
        :type: float
        """

        self._total = total

    @property
    def rate_type(self):
        """Gets the rate_type of this RateDataJsonldTeamBookGetRateCreateCollectionGetRead.  # noqa: E501


        :return: The rate_type of this RateDataJsonldTeamBookGetRateCreateCollectionGetRead.  # noqa: E501
        :rtype: str
        """
        return self._rate_type

    @rate_type.setter
    def rate_type(self, rate_type):
        """Sets the rate_type of this RateDataJsonldTeamBookGetRateCreateCollectionGetRead.


        :param rate_type: The rate_type of this RateDataJsonldTeamBookGetRateCreateCollectionGetRead.  # noqa: E501
        :type: str
        """

        self._rate_type = rate_type

    @property
    def transit_days(self):
        """Gets the transit_days of this RateDataJsonldTeamBookGetRateCreateCollectionGetRead.  # noqa: E501


        :return: The transit_days of this RateDataJsonldTeamBookGetRateCreateCollectionGetRead.  # noqa: E501
        :rtype: int
        """
        return self._transit_days

    @transit_days.setter
    def transit_days(self, transit_days):
        """Sets the transit_days of this RateDataJsonldTeamBookGetRateCreateCollectionGetRead.


        :param transit_days: The transit_days of this RateDataJsonldTeamBookGetRateCreateCollectionGetRead.  # noqa: E501
        :type: int
        """

        self._transit_days = transit_days

    @property
    def icon_url(self):
        """Gets the icon_url of this RateDataJsonldTeamBookGetRateCreateCollectionGetRead.  # noqa: E501


        :return: The icon_url of this RateDataJsonldTeamBookGetRateCreateCollectionGetRead.  # noqa: E501
        :rtype: str
        """
        return self._icon_url

    @icon_url.setter
    def icon_url(self, icon_url):
        """Sets the icon_url of this RateDataJsonldTeamBookGetRateCreateCollectionGetRead.


        :param icon_url: The icon_url of this RateDataJsonldTeamBookGetRateCreateCollectionGetRead.  # noqa: E501
        :type: str
        """

        self._icon_url = icon_url

    @property
    def rate_remarks(self):
        """Gets the rate_remarks of this RateDataJsonldTeamBookGetRateCreateCollectionGetRead.  # noqa: E501


        :return: The rate_remarks of this RateDataJsonldTeamBookGetRateCreateCollectionGetRead.  # noqa: E501
        :rtype: list[str]
        """
        return self._rate_remarks

    @rate_remarks.setter
    def rate_remarks(self, rate_remarks):
        """Sets the rate_remarks of this RateDataJsonldTeamBookGetRateCreateCollectionGetRead.


        :param rate_remarks: The rate_remarks of this RateDataJsonldTeamBookGetRateCreateCollectionGetRead.  # noqa: E501
        :type: list[str]
        """

        self._rate_remarks = rate_remarks

    @property
    def rate_break_down_list(self):
        """Gets the rate_break_down_list of this RateDataJsonldTeamBookGetRateCreateCollectionGetRead.  # noqa: E501


        :return: The rate_break_down_list of this RateDataJsonldTeamBookGetRateCreateCollectionGetRead.  # noqa: E501
        :rtype: list[RateBreakDownJsonldTeamBookGetRateCreateCollectionGetRead]
        """
        return self._rate_break_down_list

    @rate_break_down_list.setter
    def rate_break_down_list(self, rate_break_down_list):
        """Sets the rate_break_down_list of this RateDataJsonldTeamBookGetRateCreateCollectionGetRead.


        :param rate_break_down_list: The rate_break_down_list of this RateDataJsonldTeamBookGetRateCreateCollectionGetRead.  # noqa: E501
        :type: list[RateBreakDownJsonldTeamBookGetRateCreateCollectionGetRead]
        """

        self._rate_break_down_list = rate_break_down_list

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
        if issubclass(RateDataJsonldTeamBookGetRateCreateCollectionGetRead, dict):
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
        if not isinstance(other, RateDataJsonldTeamBookGetRateCreateCollectionGetRead):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
