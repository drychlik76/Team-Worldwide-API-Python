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

class InlineResponse200Hydrasearch(object):
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
        'type': 'str',
        'hydratemplate': 'str',
        'hydravariable_representation': 'str',
        'hydramapping': 'list[InlineResponse200HydrasearchHydramapping]'
    }

    attribute_map = {
        'type': '@type',
        'hydratemplate': 'hydra:template',
        'hydravariable_representation': 'hydra:variableRepresentation',
        'hydramapping': 'hydra:mapping'
    }

    def __init__(self, type=None, hydratemplate=None, hydravariable_representation=None, hydramapping=None):  # noqa: E501
        """InlineResponse200Hydrasearch - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._hydratemplate = None
        self._hydravariable_representation = None
        self._hydramapping = None
        self.discriminator = None
        if type is not None:
            self.type = type
        if hydratemplate is not None:
            self.hydratemplate = hydratemplate
        if hydravariable_representation is not None:
            self.hydravariable_representation = hydravariable_representation
        if hydramapping is not None:
            self.hydramapping = hydramapping

    @property
    def type(self):
        """Gets the type of this InlineResponse200Hydrasearch.  # noqa: E501


        :return: The type of this InlineResponse200Hydrasearch.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this InlineResponse200Hydrasearch.


        :param type: The type of this InlineResponse200Hydrasearch.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def hydratemplate(self):
        """Gets the hydratemplate of this InlineResponse200Hydrasearch.  # noqa: E501


        :return: The hydratemplate of this InlineResponse200Hydrasearch.  # noqa: E501
        :rtype: str
        """
        return self._hydratemplate

    @hydratemplate.setter
    def hydratemplate(self, hydratemplate):
        """Sets the hydratemplate of this InlineResponse200Hydrasearch.


        :param hydratemplate: The hydratemplate of this InlineResponse200Hydrasearch.  # noqa: E501
        :type: str
        """

        self._hydratemplate = hydratemplate

    @property
    def hydravariable_representation(self):
        """Gets the hydravariable_representation of this InlineResponse200Hydrasearch.  # noqa: E501


        :return: The hydravariable_representation of this InlineResponse200Hydrasearch.  # noqa: E501
        :rtype: str
        """
        return self._hydravariable_representation

    @hydravariable_representation.setter
    def hydravariable_representation(self, hydravariable_representation):
        """Sets the hydravariable_representation of this InlineResponse200Hydrasearch.


        :param hydravariable_representation: The hydravariable_representation of this InlineResponse200Hydrasearch.  # noqa: E501
        :type: str
        """

        self._hydravariable_representation = hydravariable_representation

    @property
    def hydramapping(self):
        """Gets the hydramapping of this InlineResponse200Hydrasearch.  # noqa: E501


        :return: The hydramapping of this InlineResponse200Hydrasearch.  # noqa: E501
        :rtype: list[InlineResponse200HydrasearchHydramapping]
        """
        return self._hydramapping

    @hydramapping.setter
    def hydramapping(self, hydramapping):
        """Sets the hydramapping of this InlineResponse200Hydrasearch.


        :param hydramapping: The hydramapping of this InlineResponse200Hydrasearch.  # noqa: E501
        :type: list[InlineResponse200HydrasearchHydramapping]
        """

        self._hydramapping = hydramapping

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
        if issubclass(InlineResponse200Hydrasearch, dict):
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
        if not isinstance(other, InlineResponse200Hydrasearch):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
