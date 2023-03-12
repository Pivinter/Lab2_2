import unittest
import io
import sys
from Lab2_2 import LinkedList

class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.llist = LinkedList()
        self.llist.insert_at_end(1)
        self.llist.insert_at_end(2)
        self.llist.insert_at_end(3)

    def test_insert_at_end(self):
        self.llist.insert_at_end(4)
        self.assertEqual(self.llist.head.data, 1)
        self.assertEqual(self.llist.head.next.next.next.data, 4)

    def test_insert_after_value(self):
        self.llist.insert_after_value(2, 5)
        self.assertEqual(self.llist.head.next.next.data, 5)
        self.llist.insert_after_value(3, 6)
        self.assertEqual(self.llist.head.next.next.next.next.data, 6)

    def test_print_list(self):
        captured_output = io.StringIO()                
        sys.stdout = captured_output                     
        self.llist.print_list()                           
        sys.stdout = sys.__stdout__                       
        self.assertEqual(captured_output.getvalue().strip(), "1 2 3")

if __name__ == '__main__':
    unittest.main()
