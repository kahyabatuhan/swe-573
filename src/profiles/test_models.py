from django.test import TestCase
from django.db import models
from django.contrib.auth.models import User
from records import Record


class TestModels(TestCase):

    @classmethod
    def setUpTestData(cls):
    	print("setUpTestData: Run once to set up non-modified data for all class methods.")
     	testUser = User.objects.create(username='tester', email='tester@boun.edu.tr')
     	Record.objects.create(tweet='tester tweet', score=1, owner=testUser)
    	pass

    def setUp(self):
        #print("setUp: Run once for every test method to setup clean data.")
        pass

    def test_false_is_false(self):
        print("Method: test_false_is_false.")
        self.assertFalse(False)

    #def test_false_is_true(self):
        #print("Method: test_false_is_true.")
        #self.assertTrue(False)

    def test_one_plus_one_equals_two(self):
        print("Method: test_one_plus_one_equals_two.")
        self.assertEqual(1 + 1, 2)

    def test(self):
				print("Method: test")
				testUser = User.objects.get(username='tester')
				testRecord = Record.objects.get(tweet='tester tweet')
				self.assertEqual('tester', testUser.username)
				self.assertEqual('tester tweet', testRecord.tweet)
				self.assertEqual(testRecord.owner, testUser)