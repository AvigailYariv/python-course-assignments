import unittest
from amino_acid_game_model import AminoAcidModel

class TestAminoAcidModel(unittest.TestCase):
    def setUp(self):
        self.model = AminoAcidModel()

    def test_next_question_returns_valid_key(self):
        key = self.model.next_question()
        self.assertIn(key, self.model.amino_acids)

    def test_get_display_name(self):
        self.model.current = 'alanine'
        self.assertEqual(self.model.get_display_name(), 'Ala (A)')

    def test_check_answer_correct_full_name(self):
        self.model.current = 'alanine'
        correct, msg = self.model.check_answer('alanine')
        self.assertTrue(correct)
        self.assertIn('Well done', msg)
        self.assertEqual(self.model.get_score(), 1)

    def test_check_answer_accepts_spaces_and_underscores(self):
        self.model.current = 'aspartic_acid'
        # accept with underscore
        correct1, _ = self.model.check_answer('aspartic_acid')
        # reset score for isolation
        self.model.score = 0
        self.model.current = 'aspartic_acid'
        # accept with space
        correct2, _ = self.model.check_answer('aspartic acid')
        self.assertTrue(correct1)
        self.assertTrue(correct2)

    def test_check_answer_accepts_three_and_one_letter_codes(self):
        self.model.current = 'alanine'  # display 'Ala (A)'
        ok1, _ = self.model.check_answer('Ala')
        # reset and test one-letter
        self.model.current = 'alanine'
        ok2, _ = self.model.check_answer('A')
        self.assertTrue(ok1)
        self.assertTrue(ok2)

    def test_incorrect_decreases_score_and_allows_negative(self):
        self.model.current = 'glycine'
        self.assertEqual(self.model.get_score(), 0)
        ok, _ = self.model.check_answer('wrong-answer')
        self.assertFalse(ok)
        self.assertEqual(self.model.get_score(), -1)

    def test_incorrect_then_correct_adjusts_score(self):
        self.model.current = 'glycine'
        self.model.score = 0
        ok1, _ = self.model.check_answer('bad')
        self.assertFalse(ok1)
        self.assertEqual(self.model.get_score(), -1)
        ok2, _ = self.model.check_answer('glycine')
        self.assertTrue(ok2)
        # -1 then +1 -> 0
        self.assertEqual(self.model.get_score(), 0)

    def test_check_answer_no_active_question(self):
        self.model.current = None
        ok, msg = self.model.check_answer('alanine')
        self.assertFalse(ok)
        self.assertIn('No active question', msg)

if __name__ == '__main__':
    unittest.main()
