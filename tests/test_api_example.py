import requests
import unittest
from unittest.mock import patch

class TestBookingAPI(unittest.TestCase):
    def test_get_room(self):
        response = requests.get("https://automationintesting.online/room/1")
        self.assertEqual(response.status_code, 200)
        self.assertIn("roomName", response.text)

    @patch('requests.get')
    def test_get_room_mocked(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = '{"roomName": "Mock Room"}'
        response = requests.get("https://automationintesting.online/room/1")
        self.assertEqual(response.status_code, 200)
        self.assertIn("roomName", response.text)

if __name__ == "__main__":
    unittest.main()
