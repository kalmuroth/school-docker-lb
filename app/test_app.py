import unittest
from app import tasks

class TestTasks(unittest.TestCase):
    
    def test_tasks(self):
        expected_results = [{'name': 'Task 1', 'completed': 'Yes'}, {'name': 'Task 1', 'completed': 'No'}]
        self.assertEqual(tasks(), expected_results)
        
if __name__ == '__main__':
    unittest.main()
