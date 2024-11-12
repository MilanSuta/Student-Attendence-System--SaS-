import unittest
from unittest.mock import patch

from main import add_student

class TestStudentAttendanceSystem(unittest.TestCase):
    
    @patch('mysql.connector.connect')
    def test_add_student(self, mock_connect):
        mock_connection = mock_connect.return_value
        mock_cursor = mock_connection.cursor.return_value
        
        # Test adding a student
        add_student(mock_connection, 'Jane Smith', 'jane@example.com', 'password456')
        
        mock_cursor.execute.assert_called_with(
            "INSERT INTO students (student_name, student_email, student_password) VALUES (%s, %s, %s)",
            ('Jane Smith', 'jane@example.com', 'password456')
        )
        mock_connection.commit.assert_called_once()

if __name__ == '__main__':
    unittest.main()
