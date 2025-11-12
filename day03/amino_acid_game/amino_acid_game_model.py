import random


class AminoAcidModel:
    """Game model for amino acid identification.

    Keeps track of the amino acids list, current question and score.
    This class has no GUI code and can be unit-tested independently.
    """

    def __init__(self):
        self.amino_acids = {
            'alanine': 'Ala (A)',
            'arginine': 'Arg (R)',
            'asparagine': 'Asn (N)',
            'aspartic_acid': 'Asp (D)',
            'cysteine': 'Cys (C)',
            'glutamic_acid': 'Glu (E)',
            'glutamine': 'Gln (Q)',
            'glycine': 'Gly (G)',
            'histidine': 'His (H)',
            'isoleucine': 'Ile (I)',
            'leucine': 'Leu (L)',
            'lysine': 'Lys (K)',
            'methionine': 'Met (M)',
            'phenylalanine': 'Phe (F)',
            'proline': 'Pro (P)',
            'serine': 'Ser (S)',
            'threonine': 'Thr (T)',
            'tryptophan': 'Trp (W)',
            'tyrosine': 'Tyr (Y)',
            'valine': 'Val (V)'
        }
        self.score = 0
        self.current = None

    def next_question(self):
        """Pick next random amino acid and return its key."""
        self.current = random.choice(list(self.amino_acids.keys()))
        return self.current

    def get_display_name(self, key=None):
        key = key or self.current
        return self.amino_acids.get(key, '')

    def check_answer(self, user_answer: str):
        """Check user_answer against the current amino acid.

        Returns (is_correct: bool, message: str)
        Updates score: +1 for correct, -1 for incorrect (can go negative).
        Does NOT change the current question; caller should call next_question() when moving on.
        """
        if not self.current:
            return False, "No active question"

        ua = (user_answer or "").lower().strip()
        ua_simple = ua.replace(' ', '_').replace('-', '_')

        correct_key = self.current
        accepted = {correct_key.lower(), correct_key.replace('_', ' ').lower()}
        display = self.get_display_name(correct_key)
        if '(' in display and ')' in display:
            try:
                three_letter = display.split('(')[0].strip().lower()
                one_letter = display[display.find('(')+1:display.find(')')].strip().lower()
                accepted.add(three_letter)
                accepted.add(one_letter)
            except Exception:
                pass

        accepted = {a.replace('.', '').lower() for a in accepted}

        if ua.replace('.', '') in accepted or ua_simple in accepted:
            self.score += 1
            return True, f"Well done! That was {display}!"
        else:
            self.score -= 1
            return False, "Incorrect — try again. (Score -1)"

    def get_score(self):
        return self.score
