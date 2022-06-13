# coding: utf-8

"""
    Team Worldwide API 2022

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.0.5
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.TeamWorldwideAPI.claim_api import ClaimApi  # noqa: E501
from swagger_client.rest import ApiException


class TestClaimApi(unittest.TestCase):
    """ClaimApi unit test stubs"""

    def setUp(self):
        self.api = ClaimApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_claim_collection(self):
        """Test case for get_claim_collection

        Gets collection of Team WorldWide Claims  # noqa: E501
        """
        pass

    def test_get_claim_item(self):
        """Test case for get_claim_item

        Gets a single Team WorldWide Claim  # noqa: E501
        """
        pass

    def test_post_claim_collection(self):
        """Test case for post_claim_collection

        File a single Team WorldWide Claim  # noqa: E501
        """
        pass

    def test_update_claim_item(self):
        """Test case for update_claim_item

        Update an existing Team WorldWide Claim  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
