import unittest
from unittest import mock
import python_repos


class TestPython_repos(unittest.TestCase):
    """Tests for the module python_repos."""

    def test_success_request(self):
        """Test succeed searching in the GitHub."""
        status_code = '200'
        success_send = mock.Mock(return_value=status_code)
        with mock.patch('python_repos.send_request', success_send):
            self.assertEqual(python_repos.search_github(), status_code)
    
    def test_fail_request(self):
        """Test failed searching in the GitHub."""
        status_code = '404'
        fail_send = mock.Mock(return_value=status_code)
        with mock.patch('python_repos.send_request', fail_send):
            self.assertEqual(python_repos.search_github(), status_code)


if __name__ == '__main__':
    unittest.main()
