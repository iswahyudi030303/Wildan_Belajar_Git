import unittest
from tasks.tasks_manager import TaskManager

class TestTaskManager(unittest.TestCase):
    def test_singleton_instance(self):
        # Menguji apakah hanya ada satu instance TaskManager yang dibuat
        tm1 = TaskManager()
        tm2 = TaskManager()
        self.assertIs(tm1, tm2)

    # Uji fungsionalitas lainnya

if __name__ == "__main__":
    unittest.main()
