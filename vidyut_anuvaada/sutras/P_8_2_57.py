# Sutra प.8.2.57: न ध्याख्यापॄमूर्छिमदाम्
# (Final transformations (tripāḍī)) — na DyAKyApFmUrCimadAm

from sutra_engines import apply_general

SUTRA_CODE = "प.8.2.57"
SUTRA_TEXT = "न ध्याख्यापॄमूर्छिमदाम्"
SUTRA_DESC = "(Final transformations (tripāḍī)) — na DyAKyApFmUrCimadAm"


class Sutra8257:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.2.57: अग्निः'),
		('रामः', '', 'प.8.2.57: रामः'),
		('सीता', '', 'प.8.2.57: सीता'),
	]

