#!/usr/bin/env python3
"""contains client.GithubOrgClient class - UnitTest"""
import unittest
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient
from parameterized import parameterized, parameterized_class
from fixtures import TEST_PAYLOAD


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

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test has_license method"""

        org_client = GithubOrgClient("test_org")
        result = org_client.has_license(repo, license_key)
        self.assertEqual(result, expected)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration test for GithubOrgClient"""

    @classmethod
    def setUpClass(cls):
        """Set up class method"""
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()
        cls.mock_get.side_effect = [
            Mock(json=lambda: cls.org_payload),
            Mock(json=lambda: cls.repos_payload)
        ]

    @classmethod
    def tearDownClass(cls):
        """Tear down class method"""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test public_repos method"""
        org_client = GithubOrgClient("test_org")
        repos = org_client.public_repos()
        self.assertEqual(repos, self.expected_repos)

    def test_public_repos_with_license(self):
        """Test public_repos method with license"""
        org_client = GithubOrgClient("test_org")
        repos = org_client.public_repos(license="apache-2.0")
        self.assertEqual(repos, self.apache2_repos)
