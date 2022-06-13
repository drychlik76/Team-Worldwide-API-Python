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

class RequestedPickupShipmentBookingCreate(object):
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
        '_date': 'datetime',
        'type': 'str',
        'from_time': 'datetime',
        'to_time': 'datetime',
        'on_by': 'str',
        'notes': 'str'
    }

    attribute_map = {
        '_date': 'date',
        'type': 'type',
        'from_time': 'fromTime',
        'to_time': 'toTime',
        'on_by': 'onBy',
        'notes': 'notes'
    }

    def __init__(self, _date=None, type='[R] Regular', from_time=None, to_time=None, on_by='[B] By', notes=None):  # noqa: E501
        """RequestedPickupShipmentBookingCreate - a model defined in Swagger"""  # noqa: E501
        self.__date = None
        self._type = None
        self._from_time = None
        self._to_time = None
        self._on_by = None
        self._notes = None
        self.discriminator = None
        self._date = _date
        if type is not None:
            self.type = type
        self.from_time = from_time
        self.to_time = to_time
        self.on_by = on_by
        if notes is not None:
            self.notes = notes

    @property
    def _date(self):
        """Gets the _date of this RequestedPickupShipmentBookingCreate.  # noqa: E501


        :return: The _date of this RequestedPickupShipmentBookingCreate.  # noqa: E501
        :rtype: datetime
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this RequestedPickupShipmentBookingCreate.


        :param _date: The _date of this RequestedPickupShipmentBookingCreate.  # noqa: E501
        :type: datetime
        """
        if _date is None:
            raise ValueError("Invalid value for `_date`, must not be `None`")  # noqa: E501

        self.__date = _date

    @property
    def type(self):
        """Gets the type of this RequestedPickupShipmentBookingCreate.  # noqa: E501

                      [R] Regular,              [S] Special,              [F] Customer Drop-Off,              [N] No Action            # noqa: E501

        :return: The type of this RequestedPickupShipmentBookingCreate.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this RequestedPickupShipmentBookingCreate.

                      [R] Regular,              [S] Special,              [F] Customer Drop-Off,              [N] No Action            # noqa: E501

        :param type: The type of this RequestedPickupShipmentBookingCreate.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def from_time(self):
        """Gets the from_time of this RequestedPickupShipmentBookingCreate.  # noqa: E501

        Time between  # noqa: E501

        :return: The from_time of this RequestedPickupShipmentBookingCreate.  # noqa: E501
        :rtype: datetime
        """
        return self._from_time

    @from_time.setter
    def from_time(self, from_time):
        """Sets the from_time of this RequestedPickupShipmentBookingCreate.

        Time between  # noqa: E501

        :param from_time: The from_time of this RequestedPickupShipmentBookingCreate.  # noqa: E501
        :type: datetime
        """
        if from_time is None:
            raise ValueError("Invalid value for `from_time`, must not be `None`")  # noqa: E501

        self._from_time = from_time

    @property
    def to_time(self):
        """Gets the to_time of this RequestedPickupShipmentBookingCreate.  # noqa: E501

        Time between  # noqa: E501

        :return: The to_time of this RequestedPickupShipmentBookingCreate.  # noqa: E501
        :rtype: datetime
        """
        return self._to_time

    @to_time.setter
    def to_time(self, to_time):
        """Sets the to_time of this RequestedPickupShipmentBookingCreate.

        Time between  # noqa: E501

        :param to_time: The to_time of this RequestedPickupShipmentBookingCreate.  # noqa: E501
        :type: datetime
        """
        if to_time is None:
            raise ValueError("Invalid value for `to_time`, must not be `None`")  # noqa: E501

        self._to_time = to_time

    @property
    def on_by(self):
        """Gets the on_by of this RequestedPickupShipmentBookingCreate.  # noqa: E501

                  [O] On,           [B] By            # noqa: E501

        :return: The on_by of this RequestedPickupShipmentBookingCreate.  # noqa: E501
        :rtype: str
        """
        return self._on_by

    @on_by.setter
    def on_by(self, on_by):
        """Sets the on_by of this RequestedPickupShipmentBookingCreate.

                  [O] On,           [B] By            # noqa: E501

        :param on_by: The on_by of this RequestedPickupShipmentBookingCreate.  # noqa: E501
        :type: str
        """
        if on_by is None:
            raise ValueError("Invalid value for `on_by`, must not be `None`")  # noqa: E501

        self._on_by = on_by

    @property
    def notes(self):
        """Gets the notes of this RequestedPickupShipmentBookingCreate.  # noqa: E501

        Requested pickup related notes  # noqa: E501

        :return: The notes of this RequestedPickupShipmentBookingCreate.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this RequestedPickupShipmentBookingCreate.

        Requested pickup related notes  # noqa: E501

        :param notes: The notes of this RequestedPickupShipmentBookingCreate.  # noqa: E501
        :type: str
        """

        self._notes = notes

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
        if issubclass(RequestedPickupShipmentBookingCreate, dict):
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
        if not isinstance(other, RequestedPickupShipmentBookingCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
