# Sutra प.7.2.106: तदोः सः सावनन्त्ययोः
# (Taddhita (secondary derivations)) — tadoH saH sAvanantyayoH

from sutra_engines import apply_general

SUTRA_CODE = "प.7.2.106"
SUTRA_TEXT = "तदोः सः सावनन्त्ययोः"
SUTRA_DESC = "(Taddhita (secondary derivations)) — tadoH saH sAvanantyayoH"


class Sutra72106:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.2.106: अग्निः'),
		('रामः', '', 'प.7.2.106: रामः'),
		('सीता', '', 'प.7.2.106: सीता'),
	]

