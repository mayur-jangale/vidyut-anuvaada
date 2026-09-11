# Sutra प.7.2.76: रुदादिभ्यः सार्वधातुके
# (Taddhita (secondary derivations)) — rudAdiByaH sArvaDAtuke

from sutra_engines import apply_general

SUTRA_CODE = "प.7.2.76"
SUTRA_TEXT = "रुदादिभ्यः सार्वधातुके"
SUTRA_DESC = "(Taddhita (secondary derivations)) — rudAdiByaH sArvaDAtuke"


class Sutra7276:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.2.76: अग्निः'),
		('रामः', '', 'प.7.2.76: रामः'),
		('सीता', '', 'प.7.2.76: सीता'),
	]

