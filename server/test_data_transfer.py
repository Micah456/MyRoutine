import unittest
import data_transfer as dt


class TestServer(unittest.TestCase):
    user1 = {"ID": 1, "Name": "Micah", "Stars": 5}
    user2 = {"Name": "Luke", "Stars": 10}
    user3 = {"Name": "Marlee", "Stars": 0}

    routine1 = {"ID": 1, "Name": "Good Morning", "UserID": 1}
    routine2 = {"Name": "Goodnight", "UserID": 1}

    step1 = {"ID": 2, "Name": "Brush Teeth", "Order": 0, "TimeAllotted": 2, "RoutineID": 1}
    step2 = {"ID": 3, "Name": "Get Dressed", "Order": 1, "TimeAllotted": 5, "RoutineID": 1}
    step3 = {"ID": 4, "Name": "Eat Breakfast", "Order": 2, "TimeAllotted": 20, "RoutineID": 1}
    step4 = {"Name": "Feed Cat", "Order": 3, "TimeAllotted": 3, "RoutineID": 1}
    step4_columns = "[Name], [Order], [TimeAllotted], [RoutineID]"
    step4_values = "'Feed Cat', 3, 3, 1"

    def setUp(self):
        print("####### Running Set Up #######")
        statement1 = "DELETE FROM " + dt.user_table + " WHERE Name = 'Luke' OR Name = 'Marlee'"
        statement2 =  "DELETE FROM " + dt.routine_table + " WHERE Name = 'Goodnight'"
        statement3 = "DELETE FROM " + dt.step_table + " WHERE Name = 'Feed Cat'"
        statements = [statement1, statement2, statement3]
        self.assertTrue(dt.execute_multiple_statements(statements))
        
    
    def test_parse_keys_and_values(self):
        print("######## TEST: PARSE KEYS AND VALUES #######")
        results = dt.parse_keys_and_values(self.step4)
        self.assertEqual(results.get('columns'), self.step4_columns)
        self.assertEqual(results.get('values'), self.step4_values)
    
    def test_create_user(self):
        print("######## TEST: CREATE USER #######")
        # USER ALREADY CREATED
        self.assertFalse(dt.create_object(dt.user_table, self.user1))
        # NEW USER
        self.assertTrue(dt.create_object(dt.user_table, self.user2))
        # ROUTINE ALREADY CREATED
        self.assertFalse(dt.create_object(dt.routine_table, self.routine1))
        # NEW ROUTINE
        self.assertTrue(dt.create_object(dt.routine_table, self.routine2))
        # STEP ALREADY CREATED
        self.assertFalse(dt.create_object(dt.step_table, self.step1))
        # NEW STEP
        self.assertTrue(dt.create_object(dt.step_table, self.step4))
        #dt.execute_statement("SELECT * FROM " + dt.user_table + " WHERE Name = '" + self.user2.get('Name') + "' AND Stars = " + self.users.get('Stars'))
        #When you've done your 'gets' use it in the test - make separate issue for this.

# driver code
if __name__ == '__main__':
    unittest.main()
