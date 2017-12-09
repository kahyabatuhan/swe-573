from django.test import TestCase
from django.db import models
from django.contrib.auth.models import User
from records import Record
from django.core.urlresolvers import reverse
import json

class TestModels(TestCase):

    @classmethod
    def create_user(self, username, email):
        return User.objects.create(username=username, email=email)

    @classmethod
    def create_record(self, tweet, score, owner):
        return Record.objects.create(tweet=tweet, score=score, owner=owner)

    @classmethod
    def setUpTestData(cls):
    	print("setUpTestData: Run once to set up non-modified data for all class methods.")
     	testUser = User.objects.create(username='tester', email='tester@boun.edu.tr')
     	testRecord = Record.objects.create(tweet='tester tweet', score=1, owner=testUser)
    	pass

    @classmethod    
    def is_json(self, myjson):
      try:
        json_object = json.loads(myjson)
      except ValueError, e:
        return False
      return True

    def setUp(self):
        #print("setUp: Run once for every test method to setup clean data.")
        pass

    def test_user_creation(self):
        print("Method: test_user_creation")
        u = self.create_user(username='test_user_creation', email='test_user_creation@boun.edu.tr')
        self.assertTrue(isinstance(u, User))
        self.assertEqual(u.__unicode__(), u.username)
    
    def test_record_creation(self):
        print("Method: test_record_creation")
        u = self.create_user(username='test_record_creation', email='test_record_creation@boun.edu.tr')
        r = self.create_record(tweet='test_record_creation', score=0, owner=u)
        self.assertTrue(isinstance(r, Record))
        self.assertEqual(r.__unicode__(), r.tweet)
    
    def test_user_exists(self):
		print("Method: test_user_exists")
		testUser = User.objects.get(username='tester')
		self.assertEqual('tester', testUser.username)

    def test_record_exists(self):
        print("Method: test_record_exists")
        testRecord = Record.objects.get(tweet='tester tweet')
        self.assertEqual('tester tweet', testRecord.tweet)
    
    def test_user_record_relation(self):
        print("Method: test_user_record_relation")
        testUser = User.objects.get(username='tester')
        testRecord = Record.objects.get(tweet='tester tweet')
        self.assertEqual(testRecord.owner, testUser)

    def test_twt_search(self):
        print("Method: test_twt_search")
        
        keyword = "test"
        url = reverse("search")
        resp = self.client.get(url + "?q=" + keyword)
        data = json.loads(resp.content)
        
        print("Test if Response is Success")
        self.assertEqual(resp.status_code, 200)
        print("Test if Content is Json")
        self.assertTrue(self.is_json(resp.content))
        self.assertTrue('name' in resp.content)
        self.assertTrue('score' in resp.content)
        print("Test if Content has search keyword")
        self.assertTrue(keyword in resp.content)
