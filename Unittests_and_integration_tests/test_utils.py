#!/usr/bin/env python3
""" Test function access_nested_map """
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """ Class TestAccessNestedMap """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        res = access_nested_map(nested_map, path)
        self.assertEqual(res, expected)

    # tester une lever d'exeption avec assertRaises
    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        with self.assertRaises(KeyError) as raises:
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """ Class TestGetJson """

    # Test en simulant une connection async avec unittest.mock
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch("utils.requests.get")
    def test_get_json(self, url, test_payload, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response
        result = get_json(url)
        mock_get.assert_called_once_with(url)

        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):

    def test_memoize(self):

        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        testClass = TestClass()

        with patch.object(TestClass, 'a_method', return_value=42) as mock_method:
            test1 = testClass.a_property
            test2 = testClass.a_property

            mock_method.assert_called_once()

            self.assertEqual(test1, 42)
            self.assertEqual(test2, 42)


if __name__ == '__main__':
    unittest.main()
