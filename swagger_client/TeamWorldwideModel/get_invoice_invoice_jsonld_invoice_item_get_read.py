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

class GetInvoiceInvoiceJsonldInvoiceItemGetRead(object):
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
        'context': 'OneOfGetInvoiceInvoiceJsonldInvoiceItemGetReadContext',
        'id': 'str',
        'type': 'str',
        'invoice_number': 'str',
        'control_branch': 'str',
        'company': 'str',
        'shipment_type': 'str',
        'origin': 'str',
        'destination': 'str',
        'pieces': 'int',
        'weight': 'float',
        'pickup_date': 'datetime',
        'ship_date': 'datetime',
        'status': 'str',
        'invoice_date': 'datetime',
        'customer_number': 'str',
        'customer_name': 'str',
        'description': 'str',
        'total': 'float',
        'total_invoice': 'str',
        'shipper': 'ShipperJsonldInvoiceItemGetRead',
        'consignee': 'ConsigneeJsonldInvoiceItemGetRead',
        'bill_to': 'BillToJsonldInvoiceItemGetRead',
        'invoice_detail': 'list[InvoiceDetailJsonldInvoiceItemGetRead]'
    }

    attribute_map = {
        'context': '@context',
        'id': '@id',
        'type': '@type',
        'invoice_number': 'invoiceNumber',
        'control_branch': 'controlBranch',
        'company': 'company',
        'shipment_type': 'shipmentType',
        'origin': 'origin',
        'destination': 'destination',
        'pieces': 'pieces',
        'weight': 'weight',
        'pickup_date': 'pickupDate',
        'ship_date': 'shipDate',
        'status': 'status',
        'invoice_date': 'invoiceDate',
        'customer_number': 'customerNumber',
        'customer_name': 'customerName',
        'description': 'description',
        'total': 'total',
        'total_invoice': 'totalInvoice',
        'shipper': 'shipper',
        'consignee': 'consignee',
        'bill_to': 'billTo',
        'invoice_detail': 'invoiceDetail'
    }

    def __init__(self, context=None, id=None, type=None, invoice_number=None, control_branch=None, company=None, shipment_type=None, origin=None, destination=None, pieces=None, weight=None, pickup_date=None, ship_date=None, status=None, invoice_date=None, customer_number=None, customer_name=None, description=None, total=None, total_invoice=None, shipper=None, consignee=None, bill_to=None, invoice_detail=None):  # noqa: E501
        """GetInvoiceInvoiceJsonldInvoiceItemGetRead - a model defined in Swagger"""  # noqa: E501
        self._context = None
        self._id = None
        self._type = None
        self._invoice_number = None
        self._control_branch = None
        self._company = None
        self._shipment_type = None
        self._origin = None
        self._destination = None
        self._pieces = None
        self._weight = None
        self._pickup_date = None
        self._ship_date = None
        self._status = None
        self._invoice_date = None
        self._customer_number = None
        self._customer_name = None
        self._description = None
        self._total = None
        self._total_invoice = None
        self._shipper = None
        self._consignee = None
        self._bill_to = None
        self._invoice_detail = None
        self.discriminator = None
        if context is not None:
            self.context = context
        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if invoice_number is not None:
            self.invoice_number = invoice_number
        if control_branch is not None:
            self.control_branch = control_branch
        if company is not None:
            self.company = company
        if shipment_type is not None:
            self.shipment_type = shipment_type
        if origin is not None:
            self.origin = origin
        if destination is not None:
            self.destination = destination
        if pieces is not None:
            self.pieces = pieces
        if weight is not None:
            self.weight = weight
        if pickup_date is not None:
            self.pickup_date = pickup_date
        if ship_date is not None:
            self.ship_date = ship_date
        if status is not None:
            self.status = status
        if invoice_date is not None:
            self.invoice_date = invoice_date
        if customer_number is not None:
            self.customer_number = customer_number
        if customer_name is not None:
            self.customer_name = customer_name
        if description is not None:
            self.description = description
        if total is not None:
            self.total = total
        if total_invoice is not None:
            self.total_invoice = total_invoice
        if shipper is not None:
            self.shipper = shipper
        if consignee is not None:
            self.consignee = consignee
        if bill_to is not None:
            self.bill_to = bill_to
        if invoice_detail is not None:
            self.invoice_detail = invoice_detail

    @property
    def context(self):
        """Gets the context of this GetInvoiceInvoiceJsonldInvoiceItemGetRead.  # noqa: E501


        :return: The context of this GetInvoiceInvoiceJsonldInvoiceItemGetRead.  # noqa: E501
        :rtype: OneOfGetInvoiceInvoiceJsonldInvoiceItemGetReadContext
        """
        return self._context

    @context.setter
    def context(self, context):
        """Sets the context of this GetInvoiceInvoiceJsonldInvoiceItemGetRead.


        :param context: The context of this GetInvoiceInvoiceJsonldInvoiceItemGetRead.  # noqa: E501
        :type: OneOfGetInvoiceInvoiceJsonldInvoiceItemGetReadContext
        """

        self._context = context

    @property
    def id(self):
        """Gets the id of this GetInvoiceInvoiceJsonldInvoiceItemGetRead.  # noqa: E501


        :return: The id of this GetInvoiceInvoiceJsonldInvoiceItemGetRead.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetInvoiceInvoiceJsonldInvoiceItemGetRead.


        :param id: The id of this GetInvoiceInvoiceJsonldInvoiceItemGetRead.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this GetInvoiceInvoiceJsonldInvoiceItemGetRead.  # noqa: E501


        :return: The type of this GetInvoiceInvoiceJsonldInvoiceItemGetRead.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this GetInvoiceInvoiceJsonldInvoiceItemGetRead.


        :param type: The type of this GetInvoiceInvoiceJsonldInvoiceItemGetRead.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def invoice_number(self):
        """Gets the invoice_number of this GetInvoiceInvoiceJsonldInvoiceItemGetRead.  # noqa: E501


        :return: The invoice_number of this GetInvoiceInvoiceJsonldInvoiceItemGetRead.  # noqa: E501
        :rtype: str
        """
        return self._invoice_number

    @invoice_number.setter
    def invoice_number(self, invoice_number):
        """Sets the invoice_number of this GetInvoiceInvoiceJsonldInvoiceItemGetRead.


        :param invoice_number: The invoice_number of this GetInvoiceInvoiceJsonldInvoiceItemGetRead.  # noqa: E501
        :type: str
        """

        self._invoice_number = invoice_number

    @property
    def control_branch(self):
        """Gets the control_branch of this GetInvoiceInvoiceJsonldInvoiceItemGetRead.  # noqa: E501


        :return: The control_branch of this GetInvoiceInvoiceJsonldInvoiceItemGetRead.  # noqa: E501
        :rtype: str
        """
        return self._control_branch

    @control_branch.setter
    def control_branch(self, control_branch):
        """Sets the control_branch of this GetInvoiceInvoiceJsonldInvoiceItemGetRead.


        :param control_branch: The control_branch of this GetInvoiceInvoiceJsonldInvoiceItemGetRead.  # noqa: E501
        :type: str
        """

        self._control_branch = control_branch

    @property
    def company(self):
        """Gets the company of this GetInvoiceInvoiceJsonldInvoiceItemGetRead.  # noqa: E501


        :return: The company of this GetInvoiceInvoiceJsonldInvoiceItemGetRead.  # noqa: E501
        :rtype: str
        """
        return self._company

    @company.setter
    def company(self, company):
        """Sets the company of this GetInvoiceInvoiceJsonldInvoiceItemGetRead.


        :param company: The company of this GetInvoiceInvoiceJsonldInvoiceItemGetRead.  # noqa: E501
        :type: str
        """

        self._company = company

    @property
    def shipment_type(self):
        """Gets the shipment_type of this GetInvoiceInvoiceJsonldInvoiceItemGetRead.  # noqa: E501


        :return: The shipment_type of this GetInvoiceInvoiceJsonldInvoiceItemGetRead.  # noqa: E501
        :rtype: str
        """
        return self._shipment_type

    @shipment_type.setter
    def shipment_type(self, shipment_type):
        """Sets the shipment_type of this GetInvoiceInvoiceJsonldInvoiceItemGetRead.


        :param shipment_type: The shipment_type of this GetInvoiceInvoiceJsonldInvoiceItemGetRead.  # noqa: E501
        :type: str
        """

        self._shipment_type = shipment_type

    @property
    def origin(self):
        """Gets the origin of this GetInvoiceInvoiceJsonldInvoiceItemGetRead.  # noqa: E501


        :return: The origin of this GetInvoiceInvoiceJsonldInvoiceItemGetRead.  # noqa: E501
        :rtype: str
        """
        return self._origin

    @origin.setter
    def origin(self, origin):
        """Sets the origin of this GetInvoiceInvoiceJsonldInvoiceItemGetRead.


        :param origin: The origin of this GetInvoiceInvoiceJsonldInvoiceItemGetRead.  # noqa: E501
        :type: str
        """

        self._origin = origin

    @property
    def destination(self):
        """Gets the destination of this GetInvoiceInvoiceJsonldInvoiceItemGetRead.  # noqa: E501


        :return: The destination of this GetInvoiceInvoiceJsonldInvoiceItemGetRead.  # noqa: E501
        :rtype: str
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        """Sets the destination of this GetInvoiceInvoiceJsonldInvoiceItemGetRead.


        :param destination: The destination of this GetInvoiceInvoiceJsonldInvoiceItemGetRead.  # noqa: E501
        :type: str
        """

        self._destination = destination

    @property
    def pieces(self):
        """Gets the pieces of this GetInvoiceInvoiceJsonldInvoiceItemGetRead.  # noqa: E501


        :return: The pieces of this GetInvoiceInvoiceJsonldInvoiceItemGetRead.  # noqa: E501
        :rtype: int
        """
        return self._pieces

    @pieces.setter
    def pieces(self, pieces):
        """Sets the pieces of this GetInvoiceInvoiceJsonldInvoiceItemGetRead.


        :param pieces: The pieces of this GetInvoiceInvoiceJsonldInvoiceItemGetRead.  # noqa: E501
        :type: int
        """

        self._pieces = pieces

    @property
    def weight(self):
        """Gets the weight of this GetInvoiceInvoiceJsonldInvoiceItemGetRead.  # noqa: E501


        :return: The weight of this GetInvoiceInvoiceJsonldInvoiceItemGetRead.  # noqa: E501
        :rtype: float
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this GetInvoiceInvoiceJsonldInvoiceItemGetRead.


        :param weight: The weight of this GetInvoiceInvoiceJsonldInvoiceItemGetRead.  # noqa: E501
        :type: float
        """

        self._weight = weight

    @property
    def pickup_date(self):
        """Gets the pickup_date of this GetInvoiceInvoiceJsonldInvoiceItemGetRead.  # noqa: E501


        :return: The pickup_date of this GetInvoiceInvoiceJsonldInvoiceItemGetRead.  # noqa: E501
        :rtype: datetime
        """
        return self._pickup_date

    @pickup_date.setter
    def pickup_date(self, pickup_date):
        """Sets the pickup_date of this GetInvoiceInvoiceJsonldInvoiceItemGetRead.


        :param pickup_date: The pickup_date of this GetInvoiceInvoiceJsonldInvoiceItemGetRead.  # noqa: E501
        :type: datetime
        """

        self._pickup_date = pickup_date

    @property
    def ship_date(self):
        """Gets the ship_date of this GetInvoiceInvoiceJsonldInvoiceItemGetRead.  # noqa: E501


        :return: The ship_date of this GetInvoiceInvoiceJsonldInvoiceItemGetRead.  # noqa: E501
        :rtype: datetime
        """
        return self._ship_date

    @ship_date.setter
    def ship_date(self, ship_date):
        """Sets the ship_date of this GetInvoiceInvoiceJsonldInvoiceItemGetRead.


        :param ship_date: The ship_date of this GetInvoiceInvoiceJsonldInvoiceItemGetRead.  # noqa: E501
        :type: datetime
        """

        self._ship_date = ship_date

    @property
    def status(self):
        """Gets the status of this GetInvoiceInvoiceJsonldInvoiceItemGetRead.  # noqa: E501


        :return: The status of this GetInvoiceInvoiceJsonldInvoiceItemGetRead.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this GetInvoiceInvoiceJsonldInvoiceItemGetRead.


        :param status: The status of this GetInvoiceInvoiceJsonldInvoiceItemGetRead.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def invoice_date(self):
        """Gets the invoice_date of this GetInvoiceInvoiceJsonldInvoiceItemGetRead.  # noqa: E501


        :return: The invoice_date of this GetInvoiceInvoiceJsonldInvoiceItemGetRead.  # noqa: E501
        :rtype: datetime
        """
        return self._invoice_date

    @invoice_date.setter
    def invoice_date(self, invoice_date):
        """Sets the invoice_date of this GetInvoiceInvoiceJsonldInvoiceItemGetRead.


        :param invoice_date: The invoice_date of this GetInvoiceInvoiceJsonldInvoiceItemGetRead.  # noqa: E501
        :type: datetime
        """

        self._invoice_date = invoice_date

    @property
    def customer_number(self):
        """Gets the customer_number of this GetInvoiceInvoiceJsonldInvoiceItemGetRead.  # noqa: E501


        :return: The customer_number of this GetInvoiceInvoiceJsonldInvoiceItemGetRead.  # noqa: E501
        :rtype: str
        """
        return self._customer_number

    @customer_number.setter
    def customer_number(self, customer_number):
        """Sets the customer_number of this GetInvoiceInvoiceJsonldInvoiceItemGetRead.


        :param customer_number: The customer_number of this GetInvoiceInvoiceJsonldInvoiceItemGetRead.  # noqa: E501
        :type: str
        """

        self._customer_number = customer_number

    @property
    def customer_name(self):
        """Gets the customer_name of this GetInvoiceInvoiceJsonldInvoiceItemGetRead.  # noqa: E501


        :return: The customer_name of this GetInvoiceInvoiceJsonldInvoiceItemGetRead.  # noqa: E501
        :rtype: str
        """
        return self._customer_name

    @customer_name.setter
    def customer_name(self, customer_name):
        """Sets the customer_name of this GetInvoiceInvoiceJsonldInvoiceItemGetRead.


        :param customer_name: The customer_name of this GetInvoiceInvoiceJsonldInvoiceItemGetRead.  # noqa: E501
        :type: str
        """

        self._customer_name = customer_name

    @property
    def description(self):
        """Gets the description of this GetInvoiceInvoiceJsonldInvoiceItemGetRead.  # noqa: E501


        :return: The description of this GetInvoiceInvoiceJsonldInvoiceItemGetRead.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this GetInvoiceInvoiceJsonldInvoiceItemGetRead.


        :param description: The description of this GetInvoiceInvoiceJsonldInvoiceItemGetRead.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def total(self):
        """Gets the total of this GetInvoiceInvoiceJsonldInvoiceItemGetRead.  # noqa: E501


        :return: The total of this GetInvoiceInvoiceJsonldInvoiceItemGetRead.  # noqa: E501
        :rtype: float
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this GetInvoiceInvoiceJsonldInvoiceItemGetRead.


        :param total: The total of this GetInvoiceInvoiceJsonldInvoiceItemGetRead.  # noqa: E501
        :type: float
        """

        self._total = total

    @property
    def total_invoice(self):
        """Gets the total_invoice of this GetInvoiceInvoiceJsonldInvoiceItemGetRead.  # noqa: E501


        :return: The total_invoice of this GetInvoiceInvoiceJsonldInvoiceItemGetRead.  # noqa: E501
        :rtype: str
        """
        return self._total_invoice

    @total_invoice.setter
    def total_invoice(self, total_invoice):
        """Sets the total_invoice of this GetInvoiceInvoiceJsonldInvoiceItemGetRead.


        :param total_invoice: The total_invoice of this GetInvoiceInvoiceJsonldInvoiceItemGetRead.  # noqa: E501
        :type: str
        """

        self._total_invoice = total_invoice

    @property
    def shipper(self):
        """Gets the shipper of this GetInvoiceInvoiceJsonldInvoiceItemGetRead.  # noqa: E501


        :return: The shipper of this GetInvoiceInvoiceJsonldInvoiceItemGetRead.  # noqa: E501
        :rtype: ShipperJsonldInvoiceItemGetRead
        """
        return self._shipper

    @shipper.setter
    def shipper(self, shipper):
        """Sets the shipper of this GetInvoiceInvoiceJsonldInvoiceItemGetRead.


        :param shipper: The shipper of this GetInvoiceInvoiceJsonldInvoiceItemGetRead.  # noqa: E501
        :type: ShipperJsonldInvoiceItemGetRead
        """

        self._shipper = shipper

    @property
    def consignee(self):
        """Gets the consignee of this GetInvoiceInvoiceJsonldInvoiceItemGetRead.  # noqa: E501


        :return: The consignee of this GetInvoiceInvoiceJsonldInvoiceItemGetRead.  # noqa: E501
        :rtype: ConsigneeJsonldInvoiceItemGetRead
        """
        return self._consignee

    @consignee.setter
    def consignee(self, consignee):
        """Sets the consignee of this GetInvoiceInvoiceJsonldInvoiceItemGetRead.


        :param consignee: The consignee of this GetInvoiceInvoiceJsonldInvoiceItemGetRead.  # noqa: E501
        :type: ConsigneeJsonldInvoiceItemGetRead
        """

        self._consignee = consignee

    @property
    def bill_to(self):
        """Gets the bill_to of this GetInvoiceInvoiceJsonldInvoiceItemGetRead.  # noqa: E501


        :return: The bill_to of this GetInvoiceInvoiceJsonldInvoiceItemGetRead.  # noqa: E501
        :rtype: BillToJsonldInvoiceItemGetRead
        """
        return self._bill_to

    @bill_to.setter
    def bill_to(self, bill_to):
        """Sets the bill_to of this GetInvoiceInvoiceJsonldInvoiceItemGetRead.


        :param bill_to: The bill_to of this GetInvoiceInvoiceJsonldInvoiceItemGetRead.  # noqa: E501
        :type: BillToJsonldInvoiceItemGetRead
        """

        self._bill_to = bill_to

    @property
    def invoice_detail(self):
        """Gets the invoice_detail of this GetInvoiceInvoiceJsonldInvoiceItemGetRead.  # noqa: E501


        :return: The invoice_detail of this GetInvoiceInvoiceJsonldInvoiceItemGetRead.  # noqa: E501
        :rtype: list[InvoiceDetailJsonldInvoiceItemGetRead]
        """
        return self._invoice_detail

    @invoice_detail.setter
    def invoice_detail(self, invoice_detail):
        """Sets the invoice_detail of this GetInvoiceInvoiceJsonldInvoiceItemGetRead.


        :param invoice_detail: The invoice_detail of this GetInvoiceInvoiceJsonldInvoiceItemGetRead.  # noqa: E501
        :type: list[InvoiceDetailJsonldInvoiceItemGetRead]
        """

        self._invoice_detail = invoice_detail

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
        if issubclass(GetInvoiceInvoiceJsonldInvoiceItemGetRead, dict):
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
        if not isinstance(other, GetInvoiceInvoiceJsonldInvoiceItemGetRead):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other