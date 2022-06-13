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

class ShipmentBookingV2JsonldShipmentBookingCreate(object):
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
        'context': 'OneOfShipmentBookingV2JsonldShipmentBookingCreateContext',
        'id': 'str',
        'type': 'str',
        'booked_date': 'datetime',
        'shipping_mode': 'str',
        'carrier_name': 'str',
        'origin_code': 'str',
        'destination_code': 'str',
        'vendor_code': 'str',
        'carrier_booking_number': 'str',
        'carrier_booking_number2': 'str',
        'service': 'str',
        'direct_to_consignee': 'bool',
        'override_measures': 'bool',
        'total_pieces': 'int',
        'total_weight': 'float',
        'departure_date': 'datetime',
        'departure_time': 'datetime',
        'arrival_date': 'datetime',
        'arrival_time': 'datetime',
        'booking_station': 'str',
        'general_notes': 'str',
        'shipments': 'list[ShipmentJsonldShipmentBookingCreate]'
    }

    attribute_map = {
        'context': '@context',
        'id': '@id',
        'type': '@type',
        'booked_date': 'bookedDate',
        'shipping_mode': 'shippingMode',
        'carrier_name': 'carrierName',
        'origin_code': 'originCode',
        'destination_code': 'destinationCode',
        'vendor_code': 'vendorCode',
        'carrier_booking_number': 'carrierBookingNumber',
        'carrier_booking_number2': 'carrierBookingNumber2',
        'service': 'service',
        'direct_to_consignee': 'directToConsignee',
        'override_measures': 'overrideMeasures',
        'total_pieces': 'totalPieces',
        'total_weight': 'totalWeight',
        'departure_date': 'departureDate',
        'departure_time': 'departureTime',
        'arrival_date': 'arrivalDate',
        'arrival_time': 'arrivalTime',
        'booking_station': 'bookingStation',
        'general_notes': 'generalNotes',
        'shipments': 'shipments'
    }

    def __init__(self, context=None, id=None, type=None, booked_date=None, shipping_mode='[T] Domestic/International Truck', carrier_name=None, origin_code=None, destination_code=None, vendor_code=None, carrier_booking_number=None, carrier_booking_number2=None, service='[S] Standard', direct_to_consignee=None, override_measures=None, total_pieces=None, total_weight=None, departure_date=None, departure_time=None, arrival_date=None, arrival_time=None, booking_station=None, general_notes=None, shipments=None):  # noqa: E501
        """ShipmentBookingV2JsonldShipmentBookingCreate - a model defined in Swagger"""  # noqa: E501
        self._context = None
        self._id = None
        self._type = None
        self._booked_date = None
        self._shipping_mode = None
        self._carrier_name = None
        self._origin_code = None
        self._destination_code = None
        self._vendor_code = None
        self._carrier_booking_number = None
        self._carrier_booking_number2 = None
        self._service = None
        self._direct_to_consignee = None
        self._override_measures = None
        self._total_pieces = None
        self._total_weight = None
        self._departure_date = None
        self._departure_time = None
        self._arrival_date = None
        self._arrival_time = None
        self._booking_station = None
        self._general_notes = None
        self._shipments = None
        self.discriminator = None
        if context is not None:
            self.context = context
        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if booked_date is not None:
            self.booked_date = booked_date
        self.shipping_mode = shipping_mode
        if carrier_name is not None:
            self.carrier_name = carrier_name
        if origin_code is not None:
            self.origin_code = origin_code
        if destination_code is not None:
            self.destination_code = destination_code
        if vendor_code is not None:
            self.vendor_code = vendor_code
        if carrier_booking_number is not None:
            self.carrier_booking_number = carrier_booking_number
        if carrier_booking_number2 is not None:
            self.carrier_booking_number2 = carrier_booking_number2
        self.service = service
        if direct_to_consignee is not None:
            self.direct_to_consignee = direct_to_consignee
        if override_measures is not None:
            self.override_measures = override_measures
        if total_pieces is not None:
            self.total_pieces = total_pieces
        if total_weight is not None:
            self.total_weight = total_weight
        if departure_date is not None:
            self.departure_date = departure_date
        if departure_time is not None:
            self.departure_time = departure_time
        if arrival_date is not None:
            self.arrival_date = arrival_date
        if arrival_time is not None:
            self.arrival_time = arrival_time
        if booking_station is not None:
            self.booking_station = booking_station
        if general_notes is not None:
            self.general_notes = general_notes
        self.shipments = shipments

    @property
    def context(self):
        """Gets the context of this ShipmentBookingV2JsonldShipmentBookingCreate.  # noqa: E501


        :return: The context of this ShipmentBookingV2JsonldShipmentBookingCreate.  # noqa: E501
        :rtype: OneOfShipmentBookingV2JsonldShipmentBookingCreateContext
        """
        return self._context

    @context.setter
    def context(self, context):
        """Sets the context of this ShipmentBookingV2JsonldShipmentBookingCreate.


        :param context: The context of this ShipmentBookingV2JsonldShipmentBookingCreate.  # noqa: E501
        :type: OneOfShipmentBookingV2JsonldShipmentBookingCreateContext
        """

        self._context = context

    @property
    def id(self):
        """Gets the id of this ShipmentBookingV2JsonldShipmentBookingCreate.  # noqa: E501


        :return: The id of this ShipmentBookingV2JsonldShipmentBookingCreate.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShipmentBookingV2JsonldShipmentBookingCreate.


        :param id: The id of this ShipmentBookingV2JsonldShipmentBookingCreate.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this ShipmentBookingV2JsonldShipmentBookingCreate.  # noqa: E501


        :return: The type of this ShipmentBookingV2JsonldShipmentBookingCreate.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ShipmentBookingV2JsonldShipmentBookingCreate.


        :param type: The type of this ShipmentBookingV2JsonldShipmentBookingCreate.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def booked_date(self):
        """Gets the booked_date of this ShipmentBookingV2JsonldShipmentBookingCreate.  # noqa: E501


        :return: The booked_date of this ShipmentBookingV2JsonldShipmentBookingCreate.  # noqa: E501
        :rtype: datetime
        """
        return self._booked_date

    @booked_date.setter
    def booked_date(self, booked_date):
        """Sets the booked_date of this ShipmentBookingV2JsonldShipmentBookingCreate.


        :param booked_date: The booked_date of this ShipmentBookingV2JsonldShipmentBookingCreate.  # noqa: E501
        :type: datetime
        """

        self._booked_date = booked_date

    @property
    def shipping_mode(self):
        """Gets the shipping_mode of this ShipmentBookingV2JsonldShipmentBookingCreate.  # noqa: E501

                  [DA] Domestic-Air,          [IA] International-Air,          [O] Ocean,          [T] Domestic/International Truck,          [TLN] Team Line Haul        # noqa: E501

        :return: The shipping_mode of this ShipmentBookingV2JsonldShipmentBookingCreate.  # noqa: E501
        :rtype: str
        """
        return self._shipping_mode

    @shipping_mode.setter
    def shipping_mode(self, shipping_mode):
        """Sets the shipping_mode of this ShipmentBookingV2JsonldShipmentBookingCreate.

                  [DA] Domestic-Air,          [IA] International-Air,          [O] Ocean,          [T] Domestic/International Truck,          [TLN] Team Line Haul        # noqa: E501

        :param shipping_mode: The shipping_mode of this ShipmentBookingV2JsonldShipmentBookingCreate.  # noqa: E501
        :type: str
        """
        if shipping_mode is None:
            raise ValueError("Invalid value for `shipping_mode`, must not be `None`")  # noqa: E501

        self._shipping_mode = shipping_mode

    @property
    def carrier_name(self):
        """Gets the carrier_name of this ShipmentBookingV2JsonldShipmentBookingCreate.  # noqa: E501


        :return: The carrier_name of this ShipmentBookingV2JsonldShipmentBookingCreate.  # noqa: E501
        :rtype: str
        """
        return self._carrier_name

    @carrier_name.setter
    def carrier_name(self, carrier_name):
        """Sets the carrier_name of this ShipmentBookingV2JsonldShipmentBookingCreate.


        :param carrier_name: The carrier_name of this ShipmentBookingV2JsonldShipmentBookingCreate.  # noqa: E501
        :type: str
        """

        self._carrier_name = carrier_name

    @property
    def origin_code(self):
        """Gets the origin_code of this ShipmentBookingV2JsonldShipmentBookingCreate.  # noqa: E501


        :return: The origin_code of this ShipmentBookingV2JsonldShipmentBookingCreate.  # noqa: E501
        :rtype: str
        """
        return self._origin_code

    @origin_code.setter
    def origin_code(self, origin_code):
        """Sets the origin_code of this ShipmentBookingV2JsonldShipmentBookingCreate.


        :param origin_code: The origin_code of this ShipmentBookingV2JsonldShipmentBookingCreate.  # noqa: E501
        :type: str
        """

        self._origin_code = origin_code

    @property
    def destination_code(self):
        """Gets the destination_code of this ShipmentBookingV2JsonldShipmentBookingCreate.  # noqa: E501


        :return: The destination_code of this ShipmentBookingV2JsonldShipmentBookingCreate.  # noqa: E501
        :rtype: str
        """
        return self._destination_code

    @destination_code.setter
    def destination_code(self, destination_code):
        """Sets the destination_code of this ShipmentBookingV2JsonldShipmentBookingCreate.


        :param destination_code: The destination_code of this ShipmentBookingV2JsonldShipmentBookingCreate.  # noqa: E501
        :type: str
        """

        self._destination_code = destination_code

    @property
    def vendor_code(self):
        """Gets the vendor_code of this ShipmentBookingV2JsonldShipmentBookingCreate.  # noqa: E501


        :return: The vendor_code of this ShipmentBookingV2JsonldShipmentBookingCreate.  # noqa: E501
        :rtype: str
        """
        return self._vendor_code

    @vendor_code.setter
    def vendor_code(self, vendor_code):
        """Sets the vendor_code of this ShipmentBookingV2JsonldShipmentBookingCreate.


        :param vendor_code: The vendor_code of this ShipmentBookingV2JsonldShipmentBookingCreate.  # noqa: E501
        :type: str
        """

        self._vendor_code = vendor_code

    @property
    def carrier_booking_number(self):
        """Gets the carrier_booking_number of this ShipmentBookingV2JsonldShipmentBookingCreate.  # noqa: E501

        Carrier master bill or booking number  # noqa: E501

        :return: The carrier_booking_number of this ShipmentBookingV2JsonldShipmentBookingCreate.  # noqa: E501
        :rtype: str
        """
        return self._carrier_booking_number

    @carrier_booking_number.setter
    def carrier_booking_number(self, carrier_booking_number):
        """Sets the carrier_booking_number of this ShipmentBookingV2JsonldShipmentBookingCreate.

        Carrier master bill or booking number  # noqa: E501

        :param carrier_booking_number: The carrier_booking_number of this ShipmentBookingV2JsonldShipmentBookingCreate.  # noqa: E501
        :type: str
        """

        self._carrier_booking_number = carrier_booking_number

    @property
    def carrier_booking_number2(self):
        """Gets the carrier_booking_number2 of this ShipmentBookingV2JsonldShipmentBookingCreate.  # noqa: E501

        Secondary carrier master bill or booking number  # noqa: E501

        :return: The carrier_booking_number2 of this ShipmentBookingV2JsonldShipmentBookingCreate.  # noqa: E501
        :rtype: str
        """
        return self._carrier_booking_number2

    @carrier_booking_number2.setter
    def carrier_booking_number2(self, carrier_booking_number2):
        """Sets the carrier_booking_number2 of this ShipmentBookingV2JsonldShipmentBookingCreate.

        Secondary carrier master bill or booking number  # noqa: E501

        :param carrier_booking_number2: The carrier_booking_number2 of this ShipmentBookingV2JsonldShipmentBookingCreate.  # noqa: E501
        :type: str
        """

        self._carrier_booking_number2 = carrier_booking_number2

    @property
    def service(self):
        """Gets the service of this ShipmentBookingV2JsonldShipmentBookingCreate.  # noqa: E501

                  [S] Standard,          [X] Express,          [F] Road Feeder,          [N] Over the Counter,          [W] Weekend,          [T] Truck/Line Haul,          [E] Economy,          [H] Hot Shot,          [K] Full Truck Load,          [L] Less Than Truck Load,          [U] Exclusive Use,          [R] Live Recovery,          [C] Local        # noqa: E501

        :return: The service of this ShipmentBookingV2JsonldShipmentBookingCreate.  # noqa: E501
        :rtype: str
        """
        return self._service

    @service.setter
    def service(self, service):
        """Sets the service of this ShipmentBookingV2JsonldShipmentBookingCreate.

                  [S] Standard,          [X] Express,          [F] Road Feeder,          [N] Over the Counter,          [W] Weekend,          [T] Truck/Line Haul,          [E] Economy,          [H] Hot Shot,          [K] Full Truck Load,          [L] Less Than Truck Load,          [U] Exclusive Use,          [R] Live Recovery,          [C] Local        # noqa: E501

        :param service: The service of this ShipmentBookingV2JsonldShipmentBookingCreate.  # noqa: E501
        :type: str
        """
        if service is None:
            raise ValueError("Invalid value for `service`, must not be `None`")  # noqa: E501

        self._service = service

    @property
    def direct_to_consignee(self):
        """Gets the direct_to_consignee of this ShipmentBookingV2JsonldShipmentBookingCreate.  # noqa: E501

        Ship direct to consignee  # noqa: E501

        :return: The direct_to_consignee of this ShipmentBookingV2JsonldShipmentBookingCreate.  # noqa: E501
        :rtype: bool
        """
        return self._direct_to_consignee

    @direct_to_consignee.setter
    def direct_to_consignee(self, direct_to_consignee):
        """Sets the direct_to_consignee of this ShipmentBookingV2JsonldShipmentBookingCreate.

        Ship direct to consignee  # noqa: E501

        :param direct_to_consignee: The direct_to_consignee of this ShipmentBookingV2JsonldShipmentBookingCreate.  # noqa: E501
        :type: bool
        """

        self._direct_to_consignee = direct_to_consignee

    @property
    def override_measures(self):
        """Gets the override_measures of this ShipmentBookingV2JsonldShipmentBookingCreate.  # noqa: E501

        Override Pieces/Weight/Volume  # noqa: E501

        :return: The override_measures of this ShipmentBookingV2JsonldShipmentBookingCreate.  # noqa: E501
        :rtype: bool
        """
        return self._override_measures

    @override_measures.setter
    def override_measures(self, override_measures):
        """Sets the override_measures of this ShipmentBookingV2JsonldShipmentBookingCreate.

        Override Pieces/Weight/Volume  # noqa: E501

        :param override_measures: The override_measures of this ShipmentBookingV2JsonldShipmentBookingCreate.  # noqa: E501
        :type: bool
        """

        self._override_measures = override_measures

    @property
    def total_pieces(self):
        """Gets the total_pieces of this ShipmentBookingV2JsonldShipmentBookingCreate.  # noqa: E501

        Total number of pieces  # noqa: E501

        :return: The total_pieces of this ShipmentBookingV2JsonldShipmentBookingCreate.  # noqa: E501
        :rtype: int
        """
        return self._total_pieces

    @total_pieces.setter
    def total_pieces(self, total_pieces):
        """Sets the total_pieces of this ShipmentBookingV2JsonldShipmentBookingCreate.

        Total number of pieces  # noqa: E501

        :param total_pieces: The total_pieces of this ShipmentBookingV2JsonldShipmentBookingCreate.  # noqa: E501
        :type: int
        """

        self._total_pieces = total_pieces

    @property
    def total_weight(self):
        """Gets the total_weight of this ShipmentBookingV2JsonldShipmentBookingCreate.  # noqa: E501

        Total weight of all shipments  # noqa: E501

        :return: The total_weight of this ShipmentBookingV2JsonldShipmentBookingCreate.  # noqa: E501
        :rtype: float
        """
        return self._total_weight

    @total_weight.setter
    def total_weight(self, total_weight):
        """Sets the total_weight of this ShipmentBookingV2JsonldShipmentBookingCreate.

        Total weight of all shipments  # noqa: E501

        :param total_weight: The total_weight of this ShipmentBookingV2JsonldShipmentBookingCreate.  # noqa: E501
        :type: float
        """

        self._total_weight = total_weight

    @property
    def departure_date(self):
        """Gets the departure_date of this ShipmentBookingV2JsonldShipmentBookingCreate.  # noqa: E501


        :return: The departure_date of this ShipmentBookingV2JsonldShipmentBookingCreate.  # noqa: E501
        :rtype: datetime
        """
        return self._departure_date

    @departure_date.setter
    def departure_date(self, departure_date):
        """Sets the departure_date of this ShipmentBookingV2JsonldShipmentBookingCreate.


        :param departure_date: The departure_date of this ShipmentBookingV2JsonldShipmentBookingCreate.  # noqa: E501
        :type: datetime
        """

        self._departure_date = departure_date

    @property
    def departure_time(self):
        """Gets the departure_time of this ShipmentBookingV2JsonldShipmentBookingCreate.  # noqa: E501


        :return: The departure_time of this ShipmentBookingV2JsonldShipmentBookingCreate.  # noqa: E501
        :rtype: datetime
        """
        return self._departure_time

    @departure_time.setter
    def departure_time(self, departure_time):
        """Sets the departure_time of this ShipmentBookingV2JsonldShipmentBookingCreate.


        :param departure_time: The departure_time of this ShipmentBookingV2JsonldShipmentBookingCreate.  # noqa: E501
        :type: datetime
        """

        self._departure_time = departure_time

    @property
    def arrival_date(self):
        """Gets the arrival_date of this ShipmentBookingV2JsonldShipmentBookingCreate.  # noqa: E501


        :return: The arrival_date of this ShipmentBookingV2JsonldShipmentBookingCreate.  # noqa: E501
        :rtype: datetime
        """
        return self._arrival_date

    @arrival_date.setter
    def arrival_date(self, arrival_date):
        """Sets the arrival_date of this ShipmentBookingV2JsonldShipmentBookingCreate.


        :param arrival_date: The arrival_date of this ShipmentBookingV2JsonldShipmentBookingCreate.  # noqa: E501
        :type: datetime
        """

        self._arrival_date = arrival_date

    @property
    def arrival_time(self):
        """Gets the arrival_time of this ShipmentBookingV2JsonldShipmentBookingCreate.  # noqa: E501


        :return: The arrival_time of this ShipmentBookingV2JsonldShipmentBookingCreate.  # noqa: E501
        :rtype: datetime
        """
        return self._arrival_time

    @arrival_time.setter
    def arrival_time(self, arrival_time):
        """Sets the arrival_time of this ShipmentBookingV2JsonldShipmentBookingCreate.


        :param arrival_time: The arrival_time of this ShipmentBookingV2JsonldShipmentBookingCreate.  # noqa: E501
        :type: datetime
        """

        self._arrival_time = arrival_time

    @property
    def booking_station(self):
        """Gets the booking_station of this ShipmentBookingV2JsonldShipmentBookingCreate.  # noqa: E501

        The booking station or airport code.  Generally speaking it will be airport code  # noqa: E501

        :return: The booking_station of this ShipmentBookingV2JsonldShipmentBookingCreate.  # noqa: E501
        :rtype: str
        """
        return self._booking_station

    @booking_station.setter
    def booking_station(self, booking_station):
        """Sets the booking_station of this ShipmentBookingV2JsonldShipmentBookingCreate.

        The booking station or airport code.  Generally speaking it will be airport code  # noqa: E501

        :param booking_station: The booking_station of this ShipmentBookingV2JsonldShipmentBookingCreate.  # noqa: E501
        :type: str
        """

        self._booking_station = booking_station

    @property
    def general_notes(self):
        """Gets the general_notes of this ShipmentBookingV2JsonldShipmentBookingCreate.  # noqa: E501

        General notes for the booking  # noqa: E501

        :return: The general_notes of this ShipmentBookingV2JsonldShipmentBookingCreate.  # noqa: E501
        :rtype: str
        """
        return self._general_notes

    @general_notes.setter
    def general_notes(self, general_notes):
        """Sets the general_notes of this ShipmentBookingV2JsonldShipmentBookingCreate.

        General notes for the booking  # noqa: E501

        :param general_notes: The general_notes of this ShipmentBookingV2JsonldShipmentBookingCreate.  # noqa: E501
        :type: str
        """

        self._general_notes = general_notes

    @property
    def shipments(self):
        """Gets the shipments of this ShipmentBookingV2JsonldShipmentBookingCreate.  # noqa: E501

        Shipments  # noqa: E501

        :return: The shipments of this ShipmentBookingV2JsonldShipmentBookingCreate.  # noqa: E501
        :rtype: list[ShipmentJsonldShipmentBookingCreate]
        """
        return self._shipments

    @shipments.setter
    def shipments(self, shipments):
        """Sets the shipments of this ShipmentBookingV2JsonldShipmentBookingCreate.

        Shipments  # noqa: E501

        :param shipments: The shipments of this ShipmentBookingV2JsonldShipmentBookingCreate.  # noqa: E501
        :type: list[ShipmentJsonldShipmentBookingCreate]
        """
        if shipments is None:
            raise ValueError("Invalid value for `shipments`, must not be `None`")  # noqa: E501

        self._shipments = shipments

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
        if issubclass(ShipmentBookingV2JsonldShipmentBookingCreate, dict):
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
        if not isinstance(other, ShipmentBookingV2JsonldShipmentBookingCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
