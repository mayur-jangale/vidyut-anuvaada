# Sutra प.2.3.59: विभाषोपसर्गे
# (Samasa (compound formation)) — viBAzopasarge

from sutra_engines import apply_general

SUTRA_CODE = "प.2.3.59"
SUTRA_TEXT = "विभाषोपसर्गे"
SUTRA_DESC = "(Samasa (compound formation)) — viBAzopasarge"


class Sutra2359:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

