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

class ShipmentNoteResourceJsonldShipmentBookingCreate(object):
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
        'context': 'OneOfShipmentNoteResourceJsonldShipmentBookingCreateContext',
        'id': 'str',
        'type': 'str',
        'note_type': 'str',
        'text': 'str'
    }

    attribute_map = {
        'context': '@context',
        'id': '@id',
        'type': '@type',
        'note_type': 'noteType',
        'text': 'text'
    }

    def __init__(self, context=None, id=None, type=None, note_type='[GN] General', text=None):  # noqa: E501
        """ShipmentNoteResourceJsonldShipmentBookingCreate - a model defined in Swagger"""  # noqa: E501
        self._context = None
        self._id = None
        self._type = None
        self._note_type = None
        self._text = None
        self.discriminator = None
        if context is not None:
            self.context = context
        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        self.note_type = note_type
        self.text = text

    @property
    def context(self):
        """Gets the context of this ShipmentNoteResourceJsonldShipmentBookingCreate.  # noqa: E501


        :return: The context of this ShipmentNoteResourceJsonldShipmentBookingCreate.  # noqa: E501
        :rtype: OneOfShipmentNoteResourceJsonldShipmentBookingCreateContext
        """
        return self._context

    @context.setter
    def context(self, context):
        """Sets the context of this ShipmentNoteResourceJsonldShipmentBookingCreate.


        :param context: The context of this ShipmentNoteResourceJsonldShipmentBookingCreate.  # noqa: E501
        :type: OneOfShipmentNoteResourceJsonldShipmentBookingCreateContext
        """

        self._context = context

    @property
    def id(self):
        """Gets the id of this ShipmentNoteResourceJsonldShipmentBookingCreate.  # noqa: E501


        :return: The id of this ShipmentNoteResourceJsonldShipmentBookingCreate.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShipmentNoteResourceJsonldShipmentBookingCreate.


        :param id: The id of this ShipmentNoteResourceJsonldShipmentBookingCreate.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this ShipmentNoteResourceJsonldShipmentBookingCreate.  # noqa: E501


        :return: The type of this ShipmentNoteResourceJsonldShipmentBookingCreate.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ShipmentNoteResourceJsonldShipmentBookingCreate.


        :param type: The type of this ShipmentNoteResourceJsonldShipmentBookingCreate.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def note_type(self):
        """Gets the note_type of this ShipmentNoteResourceJsonldShipmentBookingCreate.  # noqa: E501

                  [CA] Carrier,          [DL] Delivery,          [DP] Denied Party,          [DO] Document,          [GN] General,          [HB] HouseBill,          [IN] Invoice,          [PM] Permissions,          [PU] Pickup,          [PR] Procurement,          [PC] Procurement Costs,          [RC] Recap,          [RT] Routing,          [SH] Shipment,          [ST] Status,          [TK] Tracking,          [WT] WorldTrak        # noqa: E501

        :return: The note_type of this ShipmentNoteResourceJsonldShipmentBookingCreate.  # noqa: E501
        :rtype: str
        """
        return self._note_type

    @note_type.setter
    def note_type(self, note_type):
        """Sets the note_type of this ShipmentNoteResourceJsonldShipmentBookingCreate.

                  [CA] Carrier,          [DL] Delivery,          [DP] Denied Party,          [DO] Document,          [GN] General,          [HB] HouseBill,          [IN] Invoice,          [PM] Permissions,          [PU] Pickup,          [PR] Procurement,          [PC] Procurement Costs,          [RC] Recap,          [RT] Routing,          [SH] Shipment,          [ST] Status,          [TK] Tracking,          [WT] WorldTrak        # noqa: E501

        :param note_type: The note_type of this ShipmentNoteResourceJsonldShipmentBookingCreate.  # noqa: E501
        :type: str
        """
        if note_type is None:
            raise ValueError("Invalid value for `note_type`, must not be `None`")  # noqa: E501

        self._note_type = note_type

    @property
    def text(self):
        """Gets the text of this ShipmentNoteResourceJsonldShipmentBookingCreate.  # noqa: E501


        :return: The text of this ShipmentNoteResourceJsonldShipmentBookingCreate.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this ShipmentNoteResourceJsonldShipmentBookingCreate.


        :param text: The text of this ShipmentNoteResourceJsonldShipmentBookingCreate.  # noqa: E501
        :type: str
        """
        if text is None:
            raise ValueError("Invalid value for `text`, must not be `None`")  # noqa: E501

        self._text = text

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
        if issubclass(ShipmentNoteResourceJsonldShipmentBookingCreate, dict):
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
        if not isinstance(other, ShipmentNoteResourceJsonldShipmentBookingCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
