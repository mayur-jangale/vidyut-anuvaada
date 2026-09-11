# Sutra प.8.2.108: तयोर्य्वावचि संहितायाम्
# (Final transformations (tripāḍī)) — tayoryvAvaci saMhitAyAm

from sutra_engines import apply_general

SUTRA_CODE = "प.8.2.108"
SUTRA_TEXT = "तयोर्य्वावचि संहितायाम्"
SUTRA_DESC = "(Final transformations (tripāḍī)) — tayoryvAvaci saMhitAyAm"


class Sutra82108:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.2.108: अग्निः'),
		('रामः', '', 'प.8.2.108: रामः'),
		('सीता', '', 'प.8.2.108: सीता'),
	]

