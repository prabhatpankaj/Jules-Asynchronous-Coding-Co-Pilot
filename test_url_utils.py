import unittest
from unittest.mock import patch, MagicMock
import requests # For requests.exceptions.RequestException
from url_utils import get_url_status_codes

class TestGetUrlStatusCodes(unittest.TestCase):

    @patch('url_utils.requests.get')
    def test_valid_urls(self, mock_get):
        # Setup mock_get to return different responses for different URLs
        def side_effect_func(url, timeout=None):
            mock_response = MagicMock()
            if url == "http://example.com":
                mock_response.status_code = 200
            elif url == "http://another.com":
                mock_response.status_code = 201
            else:
                # Default or raise error if an unexpected URL is called
                mock_response.status_code = 404 
            return mock_response
        
        mock_get.side_effect = side_effect_func
        
        urls = ["http://example.com", "http://another.com"]
        expected = {"http://example.com": 200, "http://another.com": 201}
        self.assertEqual(get_url_status_codes(urls), expected)

    @patch('url_utils.requests.get')
    def test_invalid_urls(self, mock_get):
        mock_get.side_effect = requests.exceptions.RequestException("Test connection error")
        
        urls = ["http://fakeurl.tld", "http://anotherfake.tld"]
        expected = {"http://fakeurl.tld": None, "http://anotherfake.tld": None}
        self.assertEqual(get_url_status_codes(urls), expected)

    @patch('url_utils.requests.get')
    def test_mixed_urls(self, mock_get):
        def side_effect_func(url, timeout=None):
            if url == "http://valid.com":
                mock_response = MagicMock()
                mock_response.status_code = 200
                return mock_response
            elif url == "http://error.com":
                raise requests.exceptions.RequestException("Test connection error")
            elif url == "http://alsogood.com":
                mock_response = MagicMock()
                mock_response.status_code = 202
                return mock_response
            else:
                # Should not happen in this test
                raise ValueError(f"Unexpected URL: {url}")

        mock_get.side_effect = side_effect_func

        urls = ["http://valid.com", "http://error.com", "http://alsogood.com"]
        expected = {"http://valid.com": 200, "http://error.com": None, "http://alsogood.com": 202}
        self.assertEqual(get_url_status_codes(urls), expected)

    def test_empty_list_of_urls(self):
        # No need to mock requests.get as it won't be called
        urls = []
        expected = {}
        self.assertEqual(get_url_status_codes(urls), expected)

if __name__ == '__main__':
    unittest.main()
