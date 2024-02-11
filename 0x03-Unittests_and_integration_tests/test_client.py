#!/usr/bin/env python3
"""contains client.GithubOrgClient class - UnitTest"""
import unittest
from unittest.mock import patch
from client import GithubOrgClient
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """Test Github Org Client"""
    @parameterized.expand([
        ('google',),
        ('abc',),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock):
        """test that GithubOrgClient.org returns the correct value"""
        org_client = GithubOrgClient(org_name)
        results = org_client.org()
        self.assertEqual(results, mock.return_value)
        mock.assert_called_once
