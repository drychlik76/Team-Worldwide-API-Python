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

class UpdateTeamBookingUpdateTeamBooking(object):
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
        'carrier_booking_number': 'str',
        'carrier_booking_number2': 'str'
    }

    attribute_map = {
        'carrier_booking_number': 'carrierBookingNumber',
        'carrier_booking_number2': 'carrierBookingNumber2'
    }

    def __init__(self, carrier_booking_number=None, carrier_booking_number2=None):  # noqa: E501
        """UpdateTeamBookingUpdateTeamBooking - a model defined in Swagger"""  # noqa: E501
        self._carrier_booking_number = None
        self._carrier_booking_number2 = None
        self.discriminator = None
        if carrier_booking_number is not None:
            self.carrier_booking_number = carrier_booking_number
        if carrier_booking_number2 is not None:
            self.carrier_booking_number2 = carrier_booking_number2

    @property
    def carrier_booking_number(self):
        """Gets the carrier_booking_number of this UpdateTeamBookingUpdateTeamBooking.  # noqa: E501

        Carrier booking number  # noqa: E501

        :return: The carrier_booking_number of this UpdateTeamBookingUpdateTeamBooking.  # noqa: E501
        :rtype: str
        """
        return self._carrier_booking_number

    @carrier_booking_number.setter
    def carrier_booking_number(self, carrier_booking_number):
        """Sets the carrier_booking_number of this UpdateTeamBookingUpdateTeamBooking.

        Carrier booking number  # noqa: E501

        :param carrier_booking_number: The carrier_booking_number of this UpdateTeamBookingUpdateTeamBooking.  # noqa: E501
        :type: str
        """

        self._carrier_booking_number = carrier_booking_number

    @property
    def carrier_booking_number2(self):
        """Gets the carrier_booking_number2 of this UpdateTeamBookingUpdateTeamBooking.  # noqa: E501

        Secondary carrier booking number  # noqa: E501

        :return: The carrier_booking_number2 of this UpdateTeamBookingUpdateTeamBooking.  # noqa: E501
        :rtype: str
        """
        return self._carrier_booking_number2

    @carrier_booking_number2.setter
    def carrier_booking_number2(self, carrier_booking_number2):
        """Sets the carrier_booking_number2 of this UpdateTeamBookingUpdateTeamBooking.

        Secondary carrier booking number  # noqa: E501

        :param carrier_booking_number2: The carrier_booking_number2 of this UpdateTeamBookingUpdateTeamBooking.  # noqa: E501
        :type: str
        """

        self._carrier_booking_number2 = carrier_booking_number2

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
        if issubclass(UpdateTeamBookingUpdateTeamBooking, dict):
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
        if not isinstance(other, UpdateTeamBookingUpdateTeamBooking):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
