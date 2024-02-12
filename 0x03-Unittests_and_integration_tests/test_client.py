#!/usr/bin/env python3
"""contains client.GithubOrgClient class - UnitTest"""
import unittest
from unittest.mock import patch, PropertyMock
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

    def test_public_repos_url(self):
        """Test _public_repos_url property"""

        known_payload = {
            "repos_url": "https://api.github.com/orgs/test_org/repos"
        }

        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_org:
            mock_org.return_value = known_payload
            org_client = GithubOrgClient("test_org")
            public_repos_url = org_client._public_repos_url
            self.assertEqual(public_repos_url, known_payload["repos_url"])

    @patch('client.get_json')
    def test_public_repos(self, mock_json):
        """Test public_repos method"""

        payload = [
            {"name": "Django"},
            {"name": "Luxand"},
        ]

        mock_json.return_value = payload
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_public:
            mock_public.return_value = "hello world"
            test_class = GithubOrgClient('test')
            result = test_class.public_repos()
            expected = [item["name"] for item in payload]
            self.assertEqual(result, expected)
            mock_public.assert_called_once()
            mock_json.assert_called_once()
