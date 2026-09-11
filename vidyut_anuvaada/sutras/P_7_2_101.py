# Sutra प.7.2.101: जराया जरसन्यतरस्याम्
# (Taddhita (secondary derivations)) — jarAyA jarasanyatarasyAm

from sutra_engines import apply_general

SUTRA_CODE = "प.7.2.101"
SUTRA_TEXT = "जराया जरसन्यतरस्याम्"
SUTRA_DESC = "(Taddhita (secondary derivations)) — jarAyA jarasanyatarasyAm"


class Sutra72101:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.2.101: अग्निः'),
		('रामः', '', 'प.7.2.101: रामः'),
		('सीता', '', 'प.7.2.101: सीता'),
	]

