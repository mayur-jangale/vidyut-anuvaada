# Sutra प.5.3.28: दक्षिणोत्तराभ्यामतसुच्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — dakziRottarAByAmatasuc

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.28"
SUTRA_TEXT = "दक्षिणोत्तराभ्यामतसुच्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — dakziRottarAByAmatasuc"


class Sutra5328:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.28: अग्निः'),
		('रामः', '', 'प.5.3.28: रामः'),
		('सीता', '', 'प.5.3.28: सीता'),
	]

