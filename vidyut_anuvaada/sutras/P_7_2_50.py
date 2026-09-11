# Sutra प.7.2.50: क्लिशः क्त्वानिष्ठयोः
# (Taddhita (secondary derivations)) — kliSaH ktvAnizWayoH

from sutra_engines import apply_general

SUTRA_CODE = "प.7.2.50"
SUTRA_TEXT = "क्लिशः क्त्वानिष्ठयोः"
SUTRA_DESC = "(Taddhita (secondary derivations)) — kliSaH ktvAnizWayoH"


class Sutra7250:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.2.50: अग्निः'),
		('रामः', '', 'प.7.2.50: रामः'),
		('सीता', '', 'प.7.2.50: सीता'),
	]

