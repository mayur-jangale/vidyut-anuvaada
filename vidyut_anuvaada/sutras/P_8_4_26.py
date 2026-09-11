# Sutra प.8.4.26: छन्दस्यृदवग्रहात्
# final transformations — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.8.4.26"
SUTRA_TEXT = "छन्दस्यृदवग्रहात्"
SUTRA_DESC = "final transformations — continued"


class Sutra8426:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.4.26: अग्निः'),
		('रामः', '', 'प.8.4.26: रामः'),
		('सीता', '', 'प.8.4.26: सीता'),
	]

