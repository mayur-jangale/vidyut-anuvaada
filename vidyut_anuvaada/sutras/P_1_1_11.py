# Sutra प.1.1.11: ईदूदेद्द्विवचनं प्रगृह्यम्
# Ī, Ū, and E in dual number are considered pragṛhya (indeclinable)

from sutra_engines import apply_general

SUTRA_CODE = "प.1.1.11"
SUTRA_TEXT = "ईदूदेद्द्विवचनं प्रगृह्यम्"
SUTRA_DESC = "Ī, Ū, and E in dual number are considered pragṛhya (indeclinable)"


class Sutra1111:
	def apply(self, word, pos):
		from P_1_1 import apply_1_1_11
		return apply_1_1_11(word, pos)

	EXAMPLES = [
		('अग्नी', 'dwivacana', 'pragṛhya=none'),
		('उषा', 'dwivacana', 'pragṛhya=none'),
		('अग्निः', 'ekavacana', 'pragṛhya=none'),
		('ईदी', 'ekavacana', 'pragṛhya=ई'),
	]

