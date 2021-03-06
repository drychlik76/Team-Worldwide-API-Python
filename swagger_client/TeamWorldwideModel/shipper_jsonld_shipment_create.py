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

class ShipperJsonldShipmentCreate(object):
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
        'context': 'OneOfShipperJsonldShipmentCreateContext',
        'id': 'str',
        'type': 'str',
        'account_number': 'str',
        'name': 'str',
        'address1': 'str',
        'address2': 'str',
        'address3': 'str',
        'city': 'str',
        'state': 'str',
        'zip_code': 'str',
        'country': 'str',
        'phone': 'str',
        'fax': 'str',
        'email': 'str',
        'contact': 'str',
        'contact_phone': 'str',
        'additional_reference': 'list[AdditionalReferenceJsonldShipmentCreate]'
    }

    attribute_map = {
        'context': '@context',
        'id': '@id',
        'type': '@type',
        'account_number': 'accountNumber',
        'name': 'name',
        'address1': 'address1',
        'address2': 'address2',
        'address3': 'address3',
        'city': 'city',
        'state': 'state',
        'zip_code': 'zipCode',
        'country': 'country',
        'phone': 'phone',
        'fax': 'fax',
        'email': 'email',
        'contact': 'contact',
        'contact_phone': 'contactPhone',
        'additional_reference': 'additionalReference'
    }

    def __init__(self, context=None, id=None, type=None, account_number=None, name=None, address1=None, address2=None, address3=None, city=None, state=None, zip_code=None, country=None, phone=None, fax=None, email=None, contact=None, contact_phone=None, additional_reference=None):  # noqa: E501
        """ShipperJsonldShipmentCreate - a model defined in Swagger"""  # noqa: E501
        self._context = None
        self._id = None
        self._type = None
        self._account_number = None
        self._name = None
        self._address1 = None
        self._address2 = None
        self._address3 = None
        self._city = None
        self._state = None
        self._zip_code = None
        self._country = None
        self._phone = None
        self._fax = None
        self._email = None
        self._contact = None
        self._contact_phone = None
        self._additional_reference = None
        self.discriminator = None
        if context is not None:
            self.context = context
        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if account_number is not None:
            self.account_number = account_number
        if name is not None:
            self.name = name
        self.address1 = address1
        if address2 is not None:
            self.address2 = address2
        if address3 is not None:
            self.address3 = address3
        self.city = city
        if state is not None:
            self.state = state
        self.zip_code = zip_code
        self.country = country
        if phone is not None:
            self.phone = phone
        if fax is not None:
            self.fax = fax
        if email is not None:
            self.email = email
        if contact is not None:
            self.contact = contact
        if contact_phone is not None:
            self.contact_phone = contact_phone
        if additional_reference is not None:
            self.additional_reference = additional_reference

    @property
    def context(self):
        """Gets the context of this ShipperJsonldShipmentCreate.  # noqa: E501


        :return: The context of this ShipperJsonldShipmentCreate.  # noqa: E501
        :rtype: OneOfShipperJsonldShipmentCreateContext
        """
        return self._context

    @context.setter
    def context(self, context):
        """Sets the context of this ShipperJsonldShipmentCreate.


        :param context: The context of this ShipperJsonldShipmentCreate.  # noqa: E501
        :type: OneOfShipperJsonldShipmentCreateContext
        """

        self._context = context

    @property
    def id(self):
        """Gets the id of this ShipperJsonldShipmentCreate.  # noqa: E501


        :return: The id of this ShipperJsonldShipmentCreate.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShipperJsonldShipmentCreate.


        :param id: The id of this ShipperJsonldShipmentCreate.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this ShipperJsonldShipmentCreate.  # noqa: E501


        :return: The type of this ShipperJsonldShipmentCreate.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ShipperJsonldShipmentCreate.


        :param type: The type of this ShipperJsonldShipmentCreate.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def account_number(self):
        """Gets the account_number of this ShipperJsonldShipmentCreate.  # noqa: E501


        :return: The account_number of this ShipperJsonldShipmentCreate.  # noqa: E501
        :rtype: str
        """
        return self._account_number

    @account_number.setter
    def account_number(self, account_number):
        """Sets the account_number of this ShipperJsonldShipmentCreate.


        :param account_number: The account_number of this ShipperJsonldShipmentCreate.  # noqa: E501
        :type: str
        """

        self._account_number = account_number

    @property
    def name(self):
        """Gets the name of this ShipperJsonldShipmentCreate.  # noqa: E501


        :return: The name of this ShipperJsonldShipmentCreate.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShipperJsonldShipmentCreate.


        :param name: The name of this ShipperJsonldShipmentCreate.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def address1(self):
        """Gets the address1 of this ShipperJsonldShipmentCreate.  # noqa: E501


        :return: The address1 of this ShipperJsonldShipmentCreate.  # noqa: E501
        :rtype: str
        """
        return self._address1

    @address1.setter
    def address1(self, address1):
        """Sets the address1 of this ShipperJsonldShipmentCreate.


        :param address1: The address1 of this ShipperJsonldShipmentCreate.  # noqa: E501
        :type: str
        """
        if address1 is None:
            raise ValueError("Invalid value for `address1`, must not be `None`")  # noqa: E501

        self._address1 = address1

    @property
    def address2(self):
        """Gets the address2 of this ShipperJsonldShipmentCreate.  # noqa: E501


        :return: The address2 of this ShipperJsonldShipmentCreate.  # noqa: E501
        :rtype: str
        """
        return self._address2

    @address2.setter
    def address2(self, address2):
        """Sets the address2 of this ShipperJsonldShipmentCreate.


        :param address2: The address2 of this ShipperJsonldShipmentCreate.  # noqa: E501
        :type: str
        """

        self._address2 = address2

    @property
    def address3(self):
        """Gets the address3 of this ShipperJsonldShipmentCreate.  # noqa: E501


        :return: The address3 of this ShipperJsonldShipmentCreate.  # noqa: E501
        :rtype: str
        """
        return self._address3

    @address3.setter
    def address3(self, address3):
        """Sets the address3 of this ShipperJsonldShipmentCreate.


        :param address3: The address3 of this ShipperJsonldShipmentCreate.  # noqa: E501
        :type: str
        """

        self._address3 = address3

    @property
    def city(self):
        """Gets the city of this ShipperJsonldShipmentCreate.  # noqa: E501


        :return: The city of this ShipperJsonldShipmentCreate.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this ShipperJsonldShipmentCreate.


        :param city: The city of this ShipperJsonldShipmentCreate.  # noqa: E501
        :type: str
        """
        if city is None:
            raise ValueError("Invalid value for `city`, must not be `None`")  # noqa: E501

        self._city = city

    @property
    def state(self):
        """Gets the state of this ShipperJsonldShipmentCreate.  # noqa: E501


        :return: The state of this ShipperJsonldShipmentCreate.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ShipperJsonldShipmentCreate.


        :param state: The state of this ShipperJsonldShipmentCreate.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def zip_code(self):
        """Gets the zip_code of this ShipperJsonldShipmentCreate.  # noqa: E501


        :return: The zip_code of this ShipperJsonldShipmentCreate.  # noqa: E501
        :rtype: str
        """
        return self._zip_code

    @zip_code.setter
    def zip_code(self, zip_code):
        """Sets the zip_code of this ShipperJsonldShipmentCreate.


        :param zip_code: The zip_code of this ShipperJsonldShipmentCreate.  # noqa: E501
        :type: str
        """
        if zip_code is None:
            raise ValueError("Invalid value for `zip_code`, must not be `None`")  # noqa: E501

        self._zip_code = zip_code

    @property
    def country(self):
        """Gets the country of this ShipperJsonldShipmentCreate.  # noqa: E501


        :return: The country of this ShipperJsonldShipmentCreate.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this ShipperJsonldShipmentCreate.


        :param country: The country of this ShipperJsonldShipmentCreate.  # noqa: E501
        :type: str
        """
        if country is None:
            raise ValueError("Invalid value for `country`, must not be `None`")  # noqa: E501

        self._country = country

    @property
    def phone(self):
        """Gets the phone of this ShipperJsonldShipmentCreate.  # noqa: E501


        :return: The phone of this ShipperJsonldShipmentCreate.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this ShipperJsonldShipmentCreate.


        :param phone: The phone of this ShipperJsonldShipmentCreate.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def fax(self):
        """Gets the fax of this ShipperJsonldShipmentCreate.  # noqa: E501


        :return: The fax of this ShipperJsonldShipmentCreate.  # noqa: E501
        :rtype: str
        """
        return self._fax

    @fax.setter
    def fax(self, fax):
        """Sets the fax of this ShipperJsonldShipmentCreate.


        :param fax: The fax of this ShipperJsonldShipmentCreate.  # noqa: E501
        :type: str
        """

        self._fax = fax

    @property
    def email(self):
        """Gets the email of this ShipperJsonldShipmentCreate.  # noqa: E501


        :return: The email of this ShipperJsonldShipmentCreate.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this ShipperJsonldShipmentCreate.


        :param email: The email of this ShipperJsonldShipmentCreate.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def contact(self):
        """Gets the contact of this ShipperJsonldShipmentCreate.  # noqa: E501


        :return: The contact of this ShipperJsonldShipmentCreate.  # noqa: E501
        :rtype: str
        """
        return self._contact

    @contact.setter
    def contact(self, contact):
        """Sets the contact of this ShipperJsonldShipmentCreate.


        :param contact: The contact of this ShipperJsonldShipmentCreate.  # noqa: E501
        :type: str
        """

        self._contact = contact

    @property
    def contact_phone(self):
        """Gets the contact_phone of this ShipperJsonldShipmentCreate.  # noqa: E501


        :return: The contact_phone of this ShipperJsonldShipmentCreate.  # noqa: E501
        :rtype: str
        """
        return self._contact_phone

    @contact_phone.setter
    def contact_phone(self, contact_phone):
        """Sets the contact_phone of this ShipperJsonldShipmentCreate.


        :param contact_phone: The contact_phone of this ShipperJsonldShipmentCreate.  # noqa: E501
        :type: str
        """

        self._contact_phone = contact_phone

    @property
    def additional_reference(self):
        """Gets the additional_reference of this ShipperJsonldShipmentCreate.  # noqa: E501


        :return: The additional_reference of this ShipperJsonldShipmentCreate.  # noqa: E501
        :rtype: list[AdditionalReferenceJsonldShipmentCreate]
        """
        return self._additional_reference

    @additional_reference.setter
    def additional_reference(self, additional_reference):
        """Sets the additional_reference of this ShipperJsonldShipmentCreate.


        :param additional_reference: The additional_reference of this ShipperJsonldShipmentCreate.  # noqa: E501
        :type: list[AdditionalReferenceJsonldShipmentCreate]
        """

        self._additional_reference = additional_reference

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
        if issubclass(ShipperJsonldShipmentCreate, dict):
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
        if not isinstance(other, ShipperJsonldShipmentCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
