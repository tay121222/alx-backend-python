#!/usr/bin/env python3
"""unit test for utils.access_nested_map"""
import unittest
from parameterized import parameterized
from utils import access_nested_map
from typing import Any, Mapping, Sequence, Tuple


class TestAccessNestedMap(unittest.TestCase):
    """class that inherits from unittest.TestCase"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: Mapping[str, Any],
                               path: Sequence[str],
                               expected_result: Any) -> None:
        """test that the method returns what it is supposed to"""
        self.assertEqual(access_nested_map(nested_map, path), expected_result)
