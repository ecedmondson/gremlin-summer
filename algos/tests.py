import pytest
from .strings_and_arrays import is_rotation

@pytest.fixture
def not_rotations_of_waterbottle():
	return [
		"not a rotation",
		"",
		"a",
		"haterbottle",
		"bottlebottle",
		"bottle water",
		"bottlewater ",
		"water"
	]

@pytest.fixture
def rotations(word, pivot):
	return word[pivot:] + word[:pivot]

class SubstringRotationTests:
	def test_is_rotation_simple_word(self, rotations):
		word = "waterbottle"
		for i in range(len(word) - 1):
			self.assertTrue(rotations(word, i))
   
	def test_is_not_rotation_simple_word(self, not_rotations_of_waterbottle):
		for word in not_rotations_of_waterbottle:
			self.assertFalse(is_rotation("waterbottle", word))