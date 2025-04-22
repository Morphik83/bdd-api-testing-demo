import requests
import unittest
from unittest.mock import patch, Mock

def get_room_name(room_id):
    url = f"https://automationintesting.online/room/{room_id}"
    response = requests.get(url)
    if response.status_code == 200:
        try:
            data = response.json()
            return data.get("roomName")
        except Exception:
            return None
    return None

class TestBookingAPI(unittest.TestCase):
    def test_get_room_name_real(self):
        # This will make a real API call
        name = get_room_name(1)
        # We don't know the actual room name, but it should be a string or None
        self.assertTrue(isinstance(name, str) or name is None)

    @patch('requests.get')
    def test_get_room_name_mocked(self, mock_get):
        # Setup the mock response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"roomName": "Mock Room"}
        mock_get.return_value = mock_response

        name = get_room_name(1)
        self.assertEqual(name, "Mock Room")

if __name__ == "__main__":
    unittest.main()
