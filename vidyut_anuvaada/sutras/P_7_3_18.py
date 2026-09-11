# Sutra प.7.3.18: जे प्रोष्ठपदानाम्
# (Taddhita (secondary derivations)) — je prozWapadAnAm

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.18"
SUTRA_TEXT = "जे प्रोष्ठपदानाम्"
SUTRA_DESC = "(Taddhita (secondary derivations)) — je prozWapadAnAm"


class Sutra7318:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.18: अग्निः'),
		('रामः', '', 'प.7.3.18: रामः'),
		('सीता', '', 'प.7.3.18: सीता'),
	]

