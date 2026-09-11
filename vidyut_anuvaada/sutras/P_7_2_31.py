# Sutra प.7.2.31: ह्रु ह्वरेश्छन्दसि
# (Taddhita (secondary derivations)) — hru hvareSCandasi

from sutra_engines import apply_general

SUTRA_CODE = "प.7.2.31"
SUTRA_TEXT = "ह्रु ह्वरेश्छन्दसि"
SUTRA_DESC = "(Taddhita (secondary derivations)) — hru hvareSCandasi"


class Sutra7231:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.2.31: अग्निः'),
		('रामः', '', 'प.7.2.31: रामः'),
		('सीता', '', 'प.7.2.31: सीता'),
	]

