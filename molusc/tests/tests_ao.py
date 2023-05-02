# from pytest import *
from molusc import ao

def setup():
	print("SETUP!")

def teardown():
	print("TEAR DOWN!")

def test_ao():
	print("Testing ao.py")

def test_get_pro_sep():
	print("Testing ao.py: get_pro_sep")
	ao.get_pro_sep(1,2,3,0.4,5,6,7)
