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

class ShipmentAdditionalReferencesJsonldShipmentCreate(object):
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
        'context': 'OneOfShipmentAdditionalReferencesJsonldShipmentCreateContext',
        'id': 'str',
        'type': 'str',
        'reference_type': 'str',
        'reference': 'str'
    }

    attribute_map = {
        'context': '@context',
        'id': '@id',
        'type': '@type',
        'reference_type': 'referenceType',
        'reference': 'reference'
    }

    def __init__(self, context=None, id=None, type=None, reference_type=None, reference=None):  # noqa: E501
        """ShipmentAdditionalReferencesJsonldShipmentCreate - a model defined in Swagger"""  # noqa: E501
        self._context = None
        self._id = None
        self._type = None
        self._reference_type = None
        self._reference = None
        self.discriminator = None
        if context is not None:
            self.context = context
        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        self.reference_type = reference_type
        self.reference = reference

    @property
    def context(self):
        """Gets the context of this ShipmentAdditionalReferencesJsonldShipmentCreate.  # noqa: E501


        :return: The context of this ShipmentAdditionalReferencesJsonldShipmentCreate.  # noqa: E501
        :rtype: OneOfShipmentAdditionalReferencesJsonldShipmentCreateContext
        """
        return self._context

    @context.setter
    def context(self, context):
        """Sets the context of this ShipmentAdditionalReferencesJsonldShipmentCreate.


        :param context: The context of this ShipmentAdditionalReferencesJsonldShipmentCreate.  # noqa: E501
        :type: OneOfShipmentAdditionalReferencesJsonldShipmentCreateContext
        """

        self._context = context

    @property
    def id(self):
        """Gets the id of this ShipmentAdditionalReferencesJsonldShipmentCreate.  # noqa: E501


        :return: The id of this ShipmentAdditionalReferencesJsonldShipmentCreate.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShipmentAdditionalReferencesJsonldShipmentCreate.


        :param id: The id of this ShipmentAdditionalReferencesJsonldShipmentCreate.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this ShipmentAdditionalReferencesJsonldShipmentCreate.  # noqa: E501


        :return: The type of this ShipmentAdditionalReferencesJsonldShipmentCreate.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ShipmentAdditionalReferencesJsonldShipmentCreate.


        :param type: The type of this ShipmentAdditionalReferencesJsonldShipmentCreate.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def reference_type(self):
        """Gets the reference_type of this ShipmentAdditionalReferencesJsonldShipmentCreate.  # noqa: E501

                  [GBL] GBL/CBL#,          [RF] Reference Number (General),          [PO] Purchase Order#,          [IN] Invoice Number,          [TCN] Transportation Control Number,          [MF] Manifest Number,          [CI] Commercial Invoice,          [PK] Packing List,          [PN] Part Number ,          [VIN] Vehicle Identification Number,          [PRO] Progressive (Pro) Number,          [CTR] Container Number,          [SN] Serial Number,          [SEL] Seal Number,          [VTL] Vehicle Title Number,          [VTS] Vehicle Title State,          [SO] Service Order#,          [BTH] Booth Number,          [QTE] Quote Number,          [JN] Job Number,          [SHW] Show Name,          [SHW] Decorator,          [SHN] Show Number,          [APT] Appointment Number,          [DN] Delivery Number,          [BOL] Bill of Lading,          [PUP] Pickup Number        # noqa: E501

        :return: The reference_type of this ShipmentAdditionalReferencesJsonldShipmentCreate.  # noqa: E501
        :rtype: str
        """
        return self._reference_type

    @reference_type.setter
    def reference_type(self, reference_type):
        """Sets the reference_type of this ShipmentAdditionalReferencesJsonldShipmentCreate.

                  [GBL] GBL/CBL#,          [RF] Reference Number (General),          [PO] Purchase Order#,          [IN] Invoice Number,          [TCN] Transportation Control Number,          [MF] Manifest Number,          [CI] Commercial Invoice,          [PK] Packing List,          [PN] Part Number ,          [VIN] Vehicle Identification Number,          [PRO] Progressive (Pro) Number,          [CTR] Container Number,          [SN] Serial Number,          [SEL] Seal Number,          [VTL] Vehicle Title Number,          [VTS] Vehicle Title State,          [SO] Service Order#,          [BTH] Booth Number,          [QTE] Quote Number,          [JN] Job Number,          [SHW] Show Name,          [SHW] Decorator,          [SHN] Show Number,          [APT] Appointment Number,          [DN] Delivery Number,          [BOL] Bill of Lading,          [PUP] Pickup Number        # noqa: E501

        :param reference_type: The reference_type of this ShipmentAdditionalReferencesJsonldShipmentCreate.  # noqa: E501
        :type: str
        """
        if reference_type is None:
            raise ValueError("Invalid value for `reference_type`, must not be `None`")  # noqa: E501

        self._reference_type = reference_type

    @property
    def reference(self):
        """Gets the reference of this ShipmentAdditionalReferencesJsonldShipmentCreate.  # noqa: E501


        :return: The reference of this ShipmentAdditionalReferencesJsonldShipmentCreate.  # noqa: E501
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this ShipmentAdditionalReferencesJsonldShipmentCreate.


        :param reference: The reference of this ShipmentAdditionalReferencesJsonldShipmentCreate.  # noqa: E501
        :type: str
        """
        if reference is None:
            raise ValueError("Invalid value for `reference`, must not be `None`")  # noqa: E501

        self._reference = reference

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
        if issubclass(ShipmentAdditionalReferencesJsonldShipmentCreate, dict):
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
        if not isinstance(other, ShipmentAdditionalReferencesJsonldShipmentCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other