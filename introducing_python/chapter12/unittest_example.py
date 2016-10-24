import unittest
from string import capwords

def just_do_it(text):
    return capwords(text)


class TestCap(unittest.TestCase):

    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_one_word(self):
        text = 'duck'
        result = just_do_it(text)
        self.assertEqual(result, "Duck")

    def test_multiple_words(self):
        text = 'a veritable flock of ducks'
        result = just_do_it(text)
        self.assertEqual(result, "A Veritable Flock Of Ducks")

    def func(self):
        text = "dog"
        result = just_do_it(text)

        self.assertEqual(result, "Dog")

    def test_func(self):
        text = "dog"
        result = just_do_it(text)

        self.assertEqual(result, "Dog")

    def test_words_With_apostrophes(self):
        text = "I'm Fresh out of ideas"
        result = just_do_it(text)

        self.assertEqual(result, "I'm Fresh Out Of Ideas")

if __name__ == "__main__" :
    unittest.main()



