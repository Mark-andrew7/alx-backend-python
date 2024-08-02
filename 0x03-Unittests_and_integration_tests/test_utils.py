#!/usr/bin/env python3
"""
Unit test for utils.access_nested_map
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch, Mock
import requests


class TestAccessNestedMap(unittest.TestCase):
    """
    TestAccessNestedMap class
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        Test access_nested_map function
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """
        Test access_nested_map function with exceptions
        """
        with self.assertRaises(expected):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    TestGetJson class
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        """
        Test get_json function
        """
        with patch('requests.get') as mock_request:
            mock_request.return_value.json.return_value = test_payload
            self.assertEqual(get_json(test_url), test_payload)


class TestMemoize(unittest.TestCase):
    """
    TestMemoize class
    """

    def test_memoize(self):
        """
        Test memoize function
        """
        class TestClass:
            """
            TestClass class
            """
            def a_method(self):
                """
                a_method method
                """
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
            
        with patch.object(TestClass, 'a_method', return_value=42) as mock_method:
            tc = TestClass()
            self.assertEqual(tc.a_property, 42)
            self.assertEqual(tc.a_property, 42)
            mock_method.assert_called_once()
