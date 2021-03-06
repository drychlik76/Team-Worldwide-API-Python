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

class FreightJsonld(object):
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
        'context': 'OneOfFreightJsonldContext',
        'id': 'str',
        'type': 'str',
        'uuid': 'str',
        'quantity': 'int',
        'weight': 'float',
        'weight_type': 'str',
        'length': 'float',
        'width': 'float',
        'height': 'float',
        'package_type': 'str',
        'is_dangerous': 'bool',
        '_class': 'str',
        'commodity': 'str',
        'dangerous': 'bool',
        'freight_as_primus_data_structure': 'list[str]'
    }

    attribute_map = {
        'context': '@context',
        'id': '@id',
        'type': '@type',
        'uuid': 'uuid',
        'quantity': 'quantity',
        'weight': 'weight',
        'weight_type': 'weightType',
        'length': 'length',
        'width': 'width',
        'height': 'height',
        'package_type': 'packageType',
        'is_dangerous': 'isDangerous',
        '_class': 'class',
        'commodity': 'commodity',
        'dangerous': 'dangerous',
        'freight_as_primus_data_structure': 'freightAsPrimusDataStructure'
    }

    def __init__(self, context=None, id=None, type=None, uuid=None, quantity=None, weight=None, weight_type='each', length=None, width=None, height=None, package_type=None, is_dangerous=None, _class=None, commodity=None, dangerous=None, freight_as_primus_data_structure=None):  # noqa: E501
        """FreightJsonld - a model defined in Swagger"""  # noqa: E501
        self._context = None
        self._id = None
        self._type = None
        self._uuid = None
        self._quantity = None
        self._weight = None
        self._weight_type = None
        self._length = None
        self._width = None
        self._height = None
        self._package_type = None
        self._is_dangerous = None
        self.__class = None
        self._commodity = None
        self._dangerous = None
        self._freight_as_primus_data_structure = None
        self.discriminator = None
        if context is not None:
            self.context = context
        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if uuid is not None:
            self.uuid = uuid
        self.quantity = quantity
        self.weight = weight
        self.weight_type = weight_type
        self.length = length
        self.width = width
        self.height = height
        if package_type is not None:
            self.package_type = package_type
        self.is_dangerous = is_dangerous
        if _class is not None:
            self._class = _class
        if commodity is not None:
            self.commodity = commodity
        if dangerous is not None:
            self.dangerous = dangerous
        if freight_as_primus_data_structure is not None:
            self.freight_as_primus_data_structure = freight_as_primus_data_structure

    @property
    def context(self):
        """Gets the context of this FreightJsonld.  # noqa: E501


        :return: The context of this FreightJsonld.  # noqa: E501
        :rtype: OneOfFreightJsonldContext
        """
        return self._context

    @context.setter
    def context(self, context):
        """Sets the context of this FreightJsonld.


        :param context: The context of this FreightJsonld.  # noqa: E501
        :type: OneOfFreightJsonldContext
        """

        self._context = context

    @property
    def id(self):
        """Gets the id of this FreightJsonld.  # noqa: E501


        :return: The id of this FreightJsonld.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FreightJsonld.


        :param id: The id of this FreightJsonld.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this FreightJsonld.  # noqa: E501


        :return: The type of this FreightJsonld.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this FreightJsonld.


        :param type: The type of this FreightJsonld.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def uuid(self):
        """Gets the uuid of this FreightJsonld.  # noqa: E501

        Unique id is assigned to each freight info. This is readable only  # noqa: E501

        :return: The uuid of this FreightJsonld.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this FreightJsonld.

        Unique id is assigned to each freight info. This is readable only  # noqa: E501

        :param uuid: The uuid of this FreightJsonld.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

    @property
    def quantity(self):
        """Gets the quantity of this FreightJsonld.  # noqa: E501


        :return: The quantity of this FreightJsonld.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this FreightJsonld.


        :param quantity: The quantity of this FreightJsonld.  # noqa: E501
        :type: int
        """
        if quantity is None:
            raise ValueError("Invalid value for `quantity`, must not be `None`")  # noqa: E501

        self._quantity = quantity

    @property
    def weight(self):
        """Gets the weight of this FreightJsonld.  # noqa: E501


        :return: The weight of this FreightJsonld.  # noqa: E501
        :rtype: float
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this FreightJsonld.


        :param weight: The weight of this FreightJsonld.  # noqa: E501
        :type: float
        """
        if weight is None:
            raise ValueError("Invalid value for `weight`, must not be `None`")  # noqa: E501

        self._weight = weight

    @property
    def weight_type(self):
        """Gets the weight_type of this FreightJsonld.  # noqa: E501


        :return: The weight_type of this FreightJsonld.  # noqa: E501
        :rtype: str
        """
        return self._weight_type

    @weight_type.setter
    def weight_type(self, weight_type):
        """Sets the weight_type of this FreightJsonld.


        :param weight_type: The weight_type of this FreightJsonld.  # noqa: E501
        :type: str
        """
        if weight_type is None:
            raise ValueError("Invalid value for `weight_type`, must not be `None`")  # noqa: E501

        self._weight_type = weight_type

    @property
    def length(self):
        """Gets the length of this FreightJsonld.  # noqa: E501


        :return: The length of this FreightJsonld.  # noqa: E501
        :rtype: float
        """
        return self._length

    @length.setter
    def length(self, length):
        """Sets the length of this FreightJsonld.


        :param length: The length of this FreightJsonld.  # noqa: E501
        :type: float
        """
        if length is None:
            raise ValueError("Invalid value for `length`, must not be `None`")  # noqa: E501

        self._length = length

    @property
    def width(self):
        """Gets the width of this FreightJsonld.  # noqa: E501


        :return: The width of this FreightJsonld.  # noqa: E501
        :rtype: float
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this FreightJsonld.


        :param width: The width of this FreightJsonld.  # noqa: E501
        :type: float
        """
        if width is None:
            raise ValueError("Invalid value for `width`, must not be `None`")  # noqa: E501

        self._width = width

    @property
    def height(self):
        """Gets the height of this FreightJsonld.  # noqa: E501


        :return: The height of this FreightJsonld.  # noqa: E501
        :rtype: float
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this FreightJsonld.


        :param height: The height of this FreightJsonld.  # noqa: E501
        :type: float
        """
        if height is None:
            raise ValueError("Invalid value for `height`, must not be `None`")  # noqa: E501

        self._height = height

    @property
    def package_type(self):
        """Gets the package_type of this FreightJsonld.  # noqa: E501

                  PLT (Pallet),          CTN (Carton),          CRT (Crate),          DRM (Drum),          CON (Container),          BOX (Box),          BDL (Bundle),          ENV (Envelope),          CYL (Cylinder,          TOT (Totes),          CAS (Case),          OTH (Other)        # noqa: E501

        :return: The package_type of this FreightJsonld.  # noqa: E501
        :rtype: str
        """
        return self._package_type

    @package_type.setter
    def package_type(self, package_type):
        """Sets the package_type of this FreightJsonld.

                  PLT (Pallet),          CTN (Carton),          CRT (Crate),          DRM (Drum),          CON (Container),          BOX (Box),          BDL (Bundle),          ENV (Envelope),          CYL (Cylinder,          TOT (Totes),          CAS (Case),          OTH (Other)        # noqa: E501

        :param package_type: The package_type of this FreightJsonld.  # noqa: E501
        :type: str
        """

        self._package_type = package_type

    @property
    def is_dangerous(self):
        """Gets the is_dangerous of this FreightJsonld.  # noqa: E501

        Is this a hazardous shipment?  # noqa: E501

        :return: The is_dangerous of this FreightJsonld.  # noqa: E501
        :rtype: bool
        """
        return self._is_dangerous

    @is_dangerous.setter
    def is_dangerous(self, is_dangerous):
        """Sets the is_dangerous of this FreightJsonld.

        Is this a hazardous shipment?  # noqa: E501

        :param is_dangerous: The is_dangerous of this FreightJsonld.  # noqa: E501
        :type: bool
        """
        if is_dangerous is None:
            raise ValueError("Invalid value for `is_dangerous`, must not be `None`")  # noqa: E501

        self._is_dangerous = is_dangerous

    @property
    def _class(self):
        """Gets the _class of this FreightJsonld.  # noqa: E501

                  Note: Normally the class is auto-assigned by the rating system.           Class 50 ??? Clean Freight - Over 50 lbs,          Class 55 - Bricks, cement, mortar, hardwood flooring, cloths or rags, magazines, copy paper,          Class 60 - Car accessories & car parts, steel cables, used tires, stone blocks, glass, moldings,          Class 65 - Car parts & accessories, bottled beverages, books in boxes, conveyors, chocolate in boxes, electric cords, tile,          Class 70 - Newspapers, wooden pencils, machinery, caskets, un-assembled furniture, food items, automobile engine,          Class 77.5 - Tires, bathroom fixtures, garments, shirts/pants, snowplows,          Class 85 - Crated machinery, transmissions, clutches, doors, CDs/DVDs, motorcycle engine,          Class 92.5 - Computers, monitors, refrigerators and freezers, gas-powered generators, cabinets, kiosk or ATMs,          Class 100 - Vacuum, boat & car covers, canvas, wine cases, caskets,          CLass 110 - Cabinets, framed paintings & artwork, table saw, metalworking,          Class 125 - Small household appliances, pictures/posters in boxes, exhibit booths, vending machines,          Class 150 - ATV, jet skis, motorcycles, assembled wooden furniture, work stations,          Class 175 - Clothing, couches, stuffed furniture, metal cabinets,          Class 200 - TVs, aircraft parts, aluminum table, packaged mattresses, snowmobiles,          Class 250 - Bamboo furniture, engine hoods, mattresses and box springs, un-assembled couch, plasma TV,          Class 300 - Wood cabinets, tables, chairs, model boats, kayaks/canoes, chassis,          Class 400 - Deer antlers,          Class 500 - Bags of gold dust, ping pong balls        # noqa: E501

        :return: The _class of this FreightJsonld.  # noqa: E501
        :rtype: str
        """
        return self.__class

    @_class.setter
    def _class(self, _class):
        """Sets the _class of this FreightJsonld.

                  Note: Normally the class is auto-assigned by the rating system.           Class 50 ??? Clean Freight - Over 50 lbs,          Class 55 - Bricks, cement, mortar, hardwood flooring, cloths or rags, magazines, copy paper,          Class 60 - Car accessories & car parts, steel cables, used tires, stone blocks, glass, moldings,          Class 65 - Car parts & accessories, bottled beverages, books in boxes, conveyors, chocolate in boxes, electric cords, tile,          Class 70 - Newspapers, wooden pencils, machinery, caskets, un-assembled furniture, food items, automobile engine,          Class 77.5 - Tires, bathroom fixtures, garments, shirts/pants, snowplows,          Class 85 - Crated machinery, transmissions, clutches, doors, CDs/DVDs, motorcycle engine,          Class 92.5 - Computers, monitors, refrigerators and freezers, gas-powered generators, cabinets, kiosk or ATMs,          Class 100 - Vacuum, boat & car covers, canvas, wine cases, caskets,          CLass 110 - Cabinets, framed paintings & artwork, table saw, metalworking,          Class 125 - Small household appliances, pictures/posters in boxes, exhibit booths, vending machines,          Class 150 - ATV, jet skis, motorcycles, assembled wooden furniture, work stations,          Class 175 - Clothing, couches, stuffed furniture, metal cabinets,          Class 200 - TVs, aircraft parts, aluminum table, packaged mattresses, snowmobiles,          Class 250 - Bamboo furniture, engine hoods, mattresses and box springs, un-assembled couch, plasma TV,          Class 300 - Wood cabinets, tables, chairs, model boats, kayaks/canoes, chassis,          Class 400 - Deer antlers,          Class 500 - Bags of gold dust, ping pong balls        # noqa: E501

        :param _class: The _class of this FreightJsonld.  # noqa: E501
        :type: str
        """

        self.__class = _class

    @property
    def commodity(self):
        """Gets the commodity of this FreightJsonld.  # noqa: E501


        :return: The commodity of this FreightJsonld.  # noqa: E501
        :rtype: str
        """
        return self._commodity

    @commodity.setter
    def commodity(self, commodity):
        """Sets the commodity of this FreightJsonld.


        :param commodity: The commodity of this FreightJsonld.  # noqa: E501
        :type: str
        """

        self._commodity = commodity

    @property
    def dangerous(self):
        """Gets the dangerous of this FreightJsonld.  # noqa: E501


        :return: The dangerous of this FreightJsonld.  # noqa: E501
        :rtype: bool
        """
        return self._dangerous

    @dangerous.setter
    def dangerous(self, dangerous):
        """Sets the dangerous of this FreightJsonld.


        :param dangerous: The dangerous of this FreightJsonld.  # noqa: E501
        :type: bool
        """

        self._dangerous = dangerous

    @property
    def freight_as_primus_data_structure(self):
        """Gets the freight_as_primus_data_structure of this FreightJsonld.  # noqa: E501


        :return: The freight_as_primus_data_structure of this FreightJsonld.  # noqa: E501
        :rtype: list[str]
        """
        return self._freight_as_primus_data_structure

    @freight_as_primus_data_structure.setter
    def freight_as_primus_data_structure(self, freight_as_primus_data_structure):
        """Sets the freight_as_primus_data_structure of this FreightJsonld.


        :param freight_as_primus_data_structure: The freight_as_primus_data_structure of this FreightJsonld.  # noqa: E501
        :type: list[str]
        """

        self._freight_as_primus_data_structure = freight_as_primus_data_structure

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
        if issubclass(FreightJsonld, dict):
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
        if not isinstance(other, FreightJsonld):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
