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

class ShipmentShipmentBookingCreate(object):
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
        'is_test_shipment': 'bool',
        'house_bill': 'str',
        'control_branch': 'str',
        'company': 'str',
        'shipment_type': 'str',
        'service': 'str',
        'pickup_date': 'datetime',
        'origin': 'str',
        'destination': 'str',
        'linear_units': 'str',
        'weight_units': 'str',
        'oversize': 'str',
        'goods_description': 'str',
        'weight': 'float',
        'special_instructions': 'str',
        'declared_value': 'float',
        'shipper': 'ShipperShipmentBookingCreate',
        'consignee': 'ConsigneeShipmentBookingCreate',
        'bill_to': 'AnyOfShipmentShipmentBookingCreateBillTo',
        'requested_pickup': 'AnyOfShipmentShipmentBookingCreateRequestedPickup',
        'requested_delivery': 'AnyOfShipmentShipmentBookingCreateRequestedDelivery',
        'shipment_goods': 'list[ShipmentGoodsShipmentBookingCreate]',
        'shipment_goods_handling': 'list[ShipmentGoodsHandlingShipmentBookingCreate]',
        'shipment_notes': 'list[ShipmentNoteResourceShipmentBookingCreate]',
        'additional_references': 'list[ShipmentAdditionalReferencesShipmentBookingCreate]',
        'projected_expenses': 'list[ProjectedExpenseShipmentBookingCreate]',
        'projected_customer_charges': 'list[ProjectedCustomerChargeShipmentBookingCreate]'
    }

    attribute_map = {
        'is_test_shipment': 'isTestShipment',
        'house_bill': 'houseBill',
        'control_branch': 'controlBranch',
        'company': 'company',
        'shipment_type': 'shipmentType',
        'service': 'service',
        'pickup_date': 'pickupDate',
        'origin': 'origin',
        'destination': 'destination',
        'linear_units': 'linearUnits',
        'weight_units': 'weightUnits',
        'oversize': 'oversize',
        'goods_description': 'goodsDescription',
        'weight': 'weight',
        'special_instructions': 'specialInstructions',
        'declared_value': 'declaredValue',
        'shipper': 'shipper',
        'consignee': 'consignee',
        'bill_to': 'billTo',
        'requested_pickup': 'requestedPickup',
        'requested_delivery': 'requestedDelivery',
        'shipment_goods': 'shipmentGoods',
        'shipment_goods_handling': 'shipmentGoodsHandling',
        'shipment_notes': 'shipmentNotes',
        'additional_references': 'additionalReferences',
        'projected_expenses': 'projectedExpenses',
        'projected_customer_charges': 'projectedCustomerCharges'
    }

    def __init__(self, is_test_shipment=None, house_bill=None, control_branch=None, company='[01] TAE', shipment_type='[8] Domestic Truck', service='[3] Economy (3-day)', pickup_date=None, origin=None, destination=None, linear_units='IN', weight_units='LB', oversize='N', goods_description=None, weight=None, special_instructions=None, declared_value=None, shipper=None, consignee=None, bill_to=None, requested_pickup=None, requested_delivery=None, shipment_goods=None, shipment_goods_handling=None, shipment_notes=None, additional_references=None, projected_expenses=None, projected_customer_charges=None):  # noqa: E501
        """ShipmentShipmentBookingCreate - a model defined in Swagger"""  # noqa: E501
        self._is_test_shipment = None
        self._house_bill = None
        self._control_branch = None
        self._company = None
        self._shipment_type = None
        self._service = None
        self._pickup_date = None
        self._origin = None
        self._destination = None
        self._linear_units = None
        self._weight_units = None
        self._oversize = None
        self._goods_description = None
        self._weight = None
        self._special_instructions = None
        self._declared_value = None
        self._shipper = None
        self._consignee = None
        self._bill_to = None
        self._requested_pickup = None
        self._requested_delivery = None
        self._shipment_goods = None
        self._shipment_goods_handling = None
        self._shipment_notes = None
        self._additional_references = None
        self._projected_expenses = None
        self._projected_customer_charges = None
        self.discriminator = None
        if is_test_shipment is not None:
            self.is_test_shipment = is_test_shipment
        if house_bill is not None:
            self.house_bill = house_bill
        if control_branch is not None:
            self.control_branch = control_branch
        self.company = company
        self.shipment_type = shipment_type
        self.service = service
        self.pickup_date = pickup_date
        if origin is not None:
            self.origin = origin
        if destination is not None:
            self.destination = destination
        self.linear_units = linear_units
        self.weight_units = weight_units
        if oversize is not None:
            self.oversize = oversize
        self.goods_description = goods_description
        if weight is not None:
            self.weight = weight
        if special_instructions is not None:
            self.special_instructions = special_instructions
        if declared_value is not None:
            self.declared_value = declared_value
        self.shipper = shipper
        self.consignee = consignee
        if bill_to is not None:
            self.bill_to = bill_to
        if requested_pickup is not None:
            self.requested_pickup = requested_pickup
        if requested_delivery is not None:
            self.requested_delivery = requested_delivery
        if shipment_goods is not None:
            self.shipment_goods = shipment_goods
        if shipment_goods_handling is not None:
            self.shipment_goods_handling = shipment_goods_handling
        if shipment_notes is not None:
            self.shipment_notes = shipment_notes
        if additional_references is not None:
            self.additional_references = additional_references
        if projected_expenses is not None:
            self.projected_expenses = projected_expenses
        if projected_customer_charges is not None:
            self.projected_customer_charges = projected_customer_charges

    @property
    def is_test_shipment(self):
        """Gets the is_test_shipment of this ShipmentShipmentBookingCreate.  # noqa: E501

        Set true if this is a live shipment  # noqa: E501

        :return: The is_test_shipment of this ShipmentShipmentBookingCreate.  # noqa: E501
        :rtype: bool
        """
        return self._is_test_shipment

    @is_test_shipment.setter
    def is_test_shipment(self, is_test_shipment):
        """Sets the is_test_shipment of this ShipmentShipmentBookingCreate.

        Set true if this is a live shipment  # noqa: E501

        :param is_test_shipment: The is_test_shipment of this ShipmentShipmentBookingCreate.  # noqa: E501
        :type: bool
        """

        self._is_test_shipment = is_test_shipment

    @property
    def house_bill(self):
        """Gets the house_bill of this ShipmentShipmentBookingCreate.  # noqa: E501

        If your account is enabled to pre-reserve the house bill,               you must reserve a house bill from the /api/teamww/get-house-bill endpoint.  Leave this property blank and a house bill,              will be generated for you.  # noqa: E501

        :return: The house_bill of this ShipmentShipmentBookingCreate.  # noqa: E501
        :rtype: str
        """
        return self._house_bill

    @house_bill.setter
    def house_bill(self, house_bill):
        """Sets the house_bill of this ShipmentShipmentBookingCreate.

        If your account is enabled to pre-reserve the house bill,               you must reserve a house bill from the /api/teamww/get-house-bill endpoint.  Leave this property blank and a house bill,              will be generated for you.  # noqa: E501

        :param house_bill: The house_bill of this ShipmentShipmentBookingCreate.  # noqa: E501
        :type: str
        """

        self._house_bill = house_bill

    @property
    def control_branch(self):
        """Gets the control_branch of this ShipmentShipmentBookingCreate.  # noqa: E501

        Control branch.  Can be null.  # noqa: E501

        :return: The control_branch of this ShipmentShipmentBookingCreate.  # noqa: E501
        :rtype: str
        """
        return self._control_branch

    @control_branch.setter
    def control_branch(self, control_branch):
        """Sets the control_branch of this ShipmentShipmentBookingCreate.

        Control branch.  Can be null.  # noqa: E501

        :param control_branch: The control_branch of this ShipmentShipmentBookingCreate.  # noqa: E501
        :type: str
        """

        self._control_branch = control_branch

    @property
    def company(self):
        """Gets the company of this ShipmentShipmentBookingCreate.  # noqa: E501

                       [01] TAE,               [02] TOS,               [03] TCB,               [05] TWC,               [21] LIB,               [25] PWJ,               [27] RAV            # noqa: E501

        :return: The company of this ShipmentShipmentBookingCreate.  # noqa: E501
        :rtype: str
        """
        return self._company

    @company.setter
    def company(self, company):
        """Sets the company of this ShipmentShipmentBookingCreate.

                       [01] TAE,               [02] TOS,               [03] TCB,               [05] TWC,               [21] LIB,               [25] PWJ,               [27] RAV            # noqa: E501

        :param company: The company of this ShipmentShipmentBookingCreate.  # noqa: E501
        :type: str
        """
        if company is None:
            raise ValueError("Invalid value for `company`, must not be `None`")  # noqa: E501

        self._company = company

    @property
    def shipment_type(self):
        """Gets the shipment_type of this ShipmentShipmentBookingCreate.  # noqa: E501

                      [1] Domestic Air,              [2] International Air Export,              [3] International Air Import,              [4] Ocean Export (FMC),              [5] Ocean Export (NVOCC),              [6] Ocean Import (FMC),              [7] Ocean Import (NVOCC),              [8] Domestic Truck,              [19] Domestic Warehouse,              [20] Ocean Warehouse,              [21] International Warehouse,              [22] Intl Customs Brokerage,              [23] Ocean Customs Brokerage,              [24] Ocean Import (Unregulated),              [25] Ocean Export (Unregulated),              [26] International Truck Import,              [27] International Truck Export,              [30] International Truck,              [31] International Air,              [32] Ocean Unregulated            # noqa: E501

        :return: The shipment_type of this ShipmentShipmentBookingCreate.  # noqa: E501
        :rtype: str
        """
        return self._shipment_type

    @shipment_type.setter
    def shipment_type(self, shipment_type):
        """Sets the shipment_type of this ShipmentShipmentBookingCreate.

                      [1] Domestic Air,              [2] International Air Export,              [3] International Air Import,              [4] Ocean Export (FMC),              [5] Ocean Export (NVOCC),              [6] Ocean Import (FMC),              [7] Ocean Import (NVOCC),              [8] Domestic Truck,              [19] Domestic Warehouse,              [20] Ocean Warehouse,              [21] International Warehouse,              [22] Intl Customs Brokerage,              [23] Ocean Customs Brokerage,              [24] Ocean Import (Unregulated),              [25] Ocean Export (Unregulated),              [26] International Truck Import,              [27] International Truck Export,              [30] International Truck,              [31] International Air,              [32] Ocean Unregulated            # noqa: E501

        :param shipment_type: The shipment_type of this ShipmentShipmentBookingCreate.  # noqa: E501
        :type: str
        """
        if shipment_type is None:
            raise ValueError("Invalid value for `shipment_type`, must not be `None`")  # noqa: E501

        self._shipment_type = shipment_type

    @property
    def service(self):
        """Gets the service of this ShipmentShipmentBookingCreate.  # noqa: E501

                  [D] Same Day,          [N] Over The Counter,          [A] Overnight AM,          [P] Overnight PM,          [R] International Express,          [T] International Standard,          [M] International Economy,          [O] Other,          [Q] Charter,          [S] Standard,          [2] Standard 2 (2-day),          [3] Economy (3-day),          [5] Deferred (4-5 day),          [L] LTL,          [F] FTL,          [U] EUV/Hotshot  # noqa: E501

        :return: The service of this ShipmentShipmentBookingCreate.  # noqa: E501
        :rtype: str
        """
        return self._service

    @service.setter
    def service(self, service):
        """Sets the service of this ShipmentShipmentBookingCreate.

                  [D] Same Day,          [N] Over The Counter,          [A] Overnight AM,          [P] Overnight PM,          [R] International Express,          [T] International Standard,          [M] International Economy,          [O] Other,          [Q] Charter,          [S] Standard,          [2] Standard 2 (2-day),          [3] Economy (3-day),          [5] Deferred (4-5 day),          [L] LTL,          [F] FTL,          [U] EUV/Hotshot  # noqa: E501

        :param service: The service of this ShipmentShipmentBookingCreate.  # noqa: E501
        :type: str
        """
        if service is None:
            raise ValueError("Invalid value for `service`, must not be `None`")  # noqa: E501

        self._service = service

    @property
    def pickup_date(self):
        """Gets the pickup_date of this ShipmentShipmentBookingCreate.  # noqa: E501

        Pickup date YYYY-MM-DD  # noqa: E501

        :return: The pickup_date of this ShipmentShipmentBookingCreate.  # noqa: E501
        :rtype: datetime
        """
        return self._pickup_date

    @pickup_date.setter
    def pickup_date(self, pickup_date):
        """Sets the pickup_date of this ShipmentShipmentBookingCreate.

        Pickup date YYYY-MM-DD  # noqa: E501

        :param pickup_date: The pickup_date of this ShipmentShipmentBookingCreate.  # noqa: E501
        :type: datetime
        """
        if pickup_date is None:
            raise ValueError("Invalid value for `pickup_date`, must not be `None`")  # noqa: E501

        self._pickup_date = pickup_date

    @property
    def origin(self):
        """Gets the origin of this ShipmentShipmentBookingCreate.  # noqa: E501

        Origin location. Must be a valid Team Worldwide origin.  # noqa: E501

        :return: The origin of this ShipmentShipmentBookingCreate.  # noqa: E501
        :rtype: str
        """
        return self._origin

    @origin.setter
    def origin(self, origin):
        """Sets the origin of this ShipmentShipmentBookingCreate.

        Origin location. Must be a valid Team Worldwide origin.  # noqa: E501

        :param origin: The origin of this ShipmentShipmentBookingCreate.  # noqa: E501
        :type: str
        """

        self._origin = origin

    @property
    def destination(self):
        """Gets the destination of this ShipmentShipmentBookingCreate.  # noqa: E501

        Destination location.  Must be a valid Team Worldwide destination  # noqa: E501

        :return: The destination of this ShipmentShipmentBookingCreate.  # noqa: E501
        :rtype: str
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        """Sets the destination of this ShipmentShipmentBookingCreate.

        Destination location.  Must be a valid Team Worldwide destination  # noqa: E501

        :param destination: The destination of this ShipmentShipmentBookingCreate.  # noqa: E501
        :type: str
        """

        self._destination = destination

    @property
    def linear_units(self):
        """Gets the linear_units of this ShipmentShipmentBookingCreate.  # noqa: E501

        Acceptable values are IN and CM  # noqa: E501

        :return: The linear_units of this ShipmentShipmentBookingCreate.  # noqa: E501
        :rtype: str
        """
        return self._linear_units

    @linear_units.setter
    def linear_units(self, linear_units):
        """Sets the linear_units of this ShipmentShipmentBookingCreate.

        Acceptable values are IN and CM  # noqa: E501

        :param linear_units: The linear_units of this ShipmentShipmentBookingCreate.  # noqa: E501
        :type: str
        """
        if linear_units is None:
            raise ValueError("Invalid value for `linear_units`, must not be `None`")  # noqa: E501

        self._linear_units = linear_units

    @property
    def weight_units(self):
        """Gets the weight_units of this ShipmentShipmentBookingCreate.  # noqa: E501

        Acceptable values are LB and KG  # noqa: E501

        :return: The weight_units of this ShipmentShipmentBookingCreate.  # noqa: E501
        :rtype: str
        """
        return self._weight_units

    @weight_units.setter
    def weight_units(self, weight_units):
        """Sets the weight_units of this ShipmentShipmentBookingCreate.

        Acceptable values are LB and KG  # noqa: E501

        :param weight_units: The weight_units of this ShipmentShipmentBookingCreate.  # noqa: E501
        :type: str
        """
        if weight_units is None:
            raise ValueError("Invalid value for `weight_units`, must not be `None`")  # noqa: E501

        self._weight_units = weight_units

    @property
    def oversize(self):
        """Gets the oversize of this ShipmentShipmentBookingCreate.  # noqa: E501

        Is the shipment oversize?  # noqa: E501

        :return: The oversize of this ShipmentShipmentBookingCreate.  # noqa: E501
        :rtype: str
        """
        return self._oversize

    @oversize.setter
    def oversize(self, oversize):
        """Sets the oversize of this ShipmentShipmentBookingCreate.

        Is the shipment oversize?  # noqa: E501

        :param oversize: The oversize of this ShipmentShipmentBookingCreate.  # noqa: E501
        :type: str
        """

        self._oversize = oversize

    @property
    def goods_description(self):
        """Gets the goods_description of this ShipmentShipmentBookingCreate.  # noqa: E501

        Description of the goods  # noqa: E501

        :return: The goods_description of this ShipmentShipmentBookingCreate.  # noqa: E501
        :rtype: str
        """
        return self._goods_description

    @goods_description.setter
    def goods_description(self, goods_description):
        """Sets the goods_description of this ShipmentShipmentBookingCreate.

        Description of the goods  # noqa: E501

        :param goods_description: The goods_description of this ShipmentShipmentBookingCreate.  # noqa: E501
        :type: str
        """
        if goods_description is None:
            raise ValueError("Invalid value for `goods_description`, must not be `None`")  # noqa: E501

        self._goods_description = goods_description

    @property
    def weight(self):
        """Gets the weight of this ShipmentShipmentBookingCreate.  # noqa: E501


        :return: The weight of this ShipmentShipmentBookingCreate.  # noqa: E501
        :rtype: float
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this ShipmentShipmentBookingCreate.


        :param weight: The weight of this ShipmentShipmentBookingCreate.  # noqa: E501
        :type: float
        """

        self._weight = weight

    @property
    def special_instructions(self):
        """Gets the special_instructions of this ShipmentShipmentBookingCreate.  # noqa: E501

        Special instructions  # noqa: E501

        :return: The special_instructions of this ShipmentShipmentBookingCreate.  # noqa: E501
        :rtype: str
        """
        return self._special_instructions

    @special_instructions.setter
    def special_instructions(self, special_instructions):
        """Sets the special_instructions of this ShipmentShipmentBookingCreate.

        Special instructions  # noqa: E501

        :param special_instructions: The special_instructions of this ShipmentShipmentBookingCreate.  # noqa: E501
        :type: str
        """

        self._special_instructions = special_instructions

    @property
    def declared_value(self):
        """Gets the declared_value of this ShipmentShipmentBookingCreate.  # noqa: E501

        Declared value  # noqa: E501

        :return: The declared_value of this ShipmentShipmentBookingCreate.  # noqa: E501
        :rtype: float
        """
        return self._declared_value

    @declared_value.setter
    def declared_value(self, declared_value):
        """Sets the declared_value of this ShipmentShipmentBookingCreate.

        Declared value  # noqa: E501

        :param declared_value: The declared_value of this ShipmentShipmentBookingCreate.  # noqa: E501
        :type: float
        """

        self._declared_value = declared_value

    @property
    def shipper(self):
        """Gets the shipper of this ShipmentShipmentBookingCreate.  # noqa: E501


        :return: The shipper of this ShipmentShipmentBookingCreate.  # noqa: E501
        :rtype: ShipperShipmentBookingCreate
        """
        return self._shipper

    @shipper.setter
    def shipper(self, shipper):
        """Sets the shipper of this ShipmentShipmentBookingCreate.


        :param shipper: The shipper of this ShipmentShipmentBookingCreate.  # noqa: E501
        :type: ShipperShipmentBookingCreate
        """
        if shipper is None:
            raise ValueError("Invalid value for `shipper`, must not be `None`")  # noqa: E501

        self._shipper = shipper

    @property
    def consignee(self):
        """Gets the consignee of this ShipmentShipmentBookingCreate.  # noqa: E501


        :return: The consignee of this ShipmentShipmentBookingCreate.  # noqa: E501
        :rtype: ConsigneeShipmentBookingCreate
        """
        return self._consignee

    @consignee.setter
    def consignee(self, consignee):
        """Sets the consignee of this ShipmentShipmentBookingCreate.


        :param consignee: The consignee of this ShipmentShipmentBookingCreate.  # noqa: E501
        :type: ConsigneeShipmentBookingCreate
        """
        if consignee is None:
            raise ValueError("Invalid value for `consignee`, must not be `None`")  # noqa: E501

        self._consignee = consignee

    @property
    def bill_to(self):
        """Gets the bill_to of this ShipmentShipmentBookingCreate.  # noqa: E501

        Billing party of this shipment  # noqa: E501

        :return: The bill_to of this ShipmentShipmentBookingCreate.  # noqa: E501
        :rtype: AnyOfShipmentShipmentBookingCreateBillTo
        """
        return self._bill_to

    @bill_to.setter
    def bill_to(self, bill_to):
        """Sets the bill_to of this ShipmentShipmentBookingCreate.

        Billing party of this shipment  # noqa: E501

        :param bill_to: The bill_to of this ShipmentShipmentBookingCreate.  # noqa: E501
        :type: AnyOfShipmentShipmentBookingCreateBillTo
        """

        self._bill_to = bill_to

    @property
    def requested_pickup(self):
        """Gets the requested_pickup of this ShipmentShipmentBookingCreate.  # noqa: E501

        Requested pickup  # noqa: E501

        :return: The requested_pickup of this ShipmentShipmentBookingCreate.  # noqa: E501
        :rtype: AnyOfShipmentShipmentBookingCreateRequestedPickup
        """
        return self._requested_pickup

    @requested_pickup.setter
    def requested_pickup(self, requested_pickup):
        """Sets the requested_pickup of this ShipmentShipmentBookingCreate.

        Requested pickup  # noqa: E501

        :param requested_pickup: The requested_pickup of this ShipmentShipmentBookingCreate.  # noqa: E501
        :type: AnyOfShipmentShipmentBookingCreateRequestedPickup
        """

        self._requested_pickup = requested_pickup

    @property
    def requested_delivery(self):
        """Gets the requested_delivery of this ShipmentShipmentBookingCreate.  # noqa: E501

        Request delivery  # noqa: E501

        :return: The requested_delivery of this ShipmentShipmentBookingCreate.  # noqa: E501
        :rtype: AnyOfShipmentShipmentBookingCreateRequestedDelivery
        """
        return self._requested_delivery

    @requested_delivery.setter
    def requested_delivery(self, requested_delivery):
        """Sets the requested_delivery of this ShipmentShipmentBookingCreate.

        Request delivery  # noqa: E501

        :param requested_delivery: The requested_delivery of this ShipmentShipmentBookingCreate.  # noqa: E501
        :type: AnyOfShipmentShipmentBookingCreateRequestedDelivery
        """

        self._requested_delivery = requested_delivery

    @property
    def shipment_goods(self):
        """Gets the shipment_goods of this ShipmentShipmentBookingCreate.  # noqa: E501

        Shipment goods  # noqa: E501

        :return: The shipment_goods of this ShipmentShipmentBookingCreate.  # noqa: E501
        :rtype: list[ShipmentGoodsShipmentBookingCreate]
        """
        return self._shipment_goods

    @shipment_goods.setter
    def shipment_goods(self, shipment_goods):
        """Sets the shipment_goods of this ShipmentShipmentBookingCreate.

        Shipment goods  # noqa: E501

        :param shipment_goods: The shipment_goods of this ShipmentShipmentBookingCreate.  # noqa: E501
        :type: list[ShipmentGoodsShipmentBookingCreate]
        """

        self._shipment_goods = shipment_goods

    @property
    def shipment_goods_handling(self):
        """Gets the shipment_goods_handling of this ShipmentShipmentBookingCreate.  # noqa: E501

        Shipment goods handling  # noqa: E501

        :return: The shipment_goods_handling of this ShipmentShipmentBookingCreate.  # noqa: E501
        :rtype: list[ShipmentGoodsHandlingShipmentBookingCreate]
        """
        return self._shipment_goods_handling

    @shipment_goods_handling.setter
    def shipment_goods_handling(self, shipment_goods_handling):
        """Sets the shipment_goods_handling of this ShipmentShipmentBookingCreate.

        Shipment goods handling  # noqa: E501

        :param shipment_goods_handling: The shipment_goods_handling of this ShipmentShipmentBookingCreate.  # noqa: E501
        :type: list[ShipmentGoodsHandlingShipmentBookingCreate]
        """

        self._shipment_goods_handling = shipment_goods_handling

    @property
    def shipment_notes(self):
        """Gets the shipment_notes of this ShipmentShipmentBookingCreate.  # noqa: E501

        Shipment notes  # noqa: E501

        :return: The shipment_notes of this ShipmentShipmentBookingCreate.  # noqa: E501
        :rtype: list[ShipmentNoteResourceShipmentBookingCreate]
        """
        return self._shipment_notes

    @shipment_notes.setter
    def shipment_notes(self, shipment_notes):
        """Sets the shipment_notes of this ShipmentShipmentBookingCreate.

        Shipment notes  # noqa: E501

        :param shipment_notes: The shipment_notes of this ShipmentShipmentBookingCreate.  # noqa: E501
        :type: list[ShipmentNoteResourceShipmentBookingCreate]
        """

        self._shipment_notes = shipment_notes

    @property
    def additional_references(self):
        """Gets the additional_references of this ShipmentShipmentBookingCreate.  # noqa: E501

        Any additional references for this shipment  # noqa: E501

        :return: The additional_references of this ShipmentShipmentBookingCreate.  # noqa: E501
        :rtype: list[ShipmentAdditionalReferencesShipmentBookingCreate]
        """
        return self._additional_references

    @additional_references.setter
    def additional_references(self, additional_references):
        """Sets the additional_references of this ShipmentShipmentBookingCreate.

        Any additional references for this shipment  # noqa: E501

        :param additional_references: The additional_references of this ShipmentShipmentBookingCreate.  # noqa: E501
        :type: list[ShipmentAdditionalReferencesShipmentBookingCreate]
        """

        self._additional_references = additional_references

    @property
    def projected_expenses(self):
        """Gets the projected_expenses of this ShipmentShipmentBookingCreate.  # noqa: E501

        Projected Expenses  # noqa: E501

        :return: The projected_expenses of this ShipmentShipmentBookingCreate.  # noqa: E501
        :rtype: list[ProjectedExpenseShipmentBookingCreate]
        """
        return self._projected_expenses

    @projected_expenses.setter
    def projected_expenses(self, projected_expenses):
        """Sets the projected_expenses of this ShipmentShipmentBookingCreate.

        Projected Expenses  # noqa: E501

        :param projected_expenses: The projected_expenses of this ShipmentShipmentBookingCreate.  # noqa: E501
        :type: list[ProjectedExpenseShipmentBookingCreate]
        """

        self._projected_expenses = projected_expenses

    @property
    def projected_customer_charges(self):
        """Gets the projected_customer_charges of this ShipmentShipmentBookingCreate.  # noqa: E501

        Projected customer charges  # noqa: E501

        :return: The projected_customer_charges of this ShipmentShipmentBookingCreate.  # noqa: E501
        :rtype: list[ProjectedCustomerChargeShipmentBookingCreate]
        """
        return self._projected_customer_charges

    @projected_customer_charges.setter
    def projected_customer_charges(self, projected_customer_charges):
        """Sets the projected_customer_charges of this ShipmentShipmentBookingCreate.

        Projected customer charges  # noqa: E501

        :param projected_customer_charges: The projected_customer_charges of this ShipmentShipmentBookingCreate.  # noqa: E501
        :type: list[ProjectedCustomerChargeShipmentBookingCreate]
        """

        self._projected_customer_charges = projected_customer_charges

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
        if issubclass(ShipmentShipmentBookingCreate, dict):
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
        if not isinstance(other, ShipmentShipmentBookingCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
