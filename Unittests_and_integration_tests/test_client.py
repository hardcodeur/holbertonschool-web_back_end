import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch("client.get_json")
    def test_org(self, org_name, mock_get_json):
        expected_result = {"login": org_name}
        mock_get_json.return_value = expected_result

        client = GithubOrgClient(org_name)

        result = client.org

        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )

        self.assertEqual(result, expected_result)

    def test_public_repos_url(self):
        mock_payload = {
            "repos_url": "https://api.github.com/orgs/test-org/repos"
        }

        with patch.object(GithubOrgClient, 'org', return_value=mock_payload):
            client = GithubOrgClient("test-org")
            result = client._public_repos_url
            expected_result = mock_payload["repos_url"]
            self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
