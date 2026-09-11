# Sutra प.2.3.57: व्यवहृपणोः समर्थयोः
# (Samasa (compound formation)) — vyavahfpaRoH samarTayoH

from sutra_engines import apply_general

SUTRA_CODE = "प.2.3.57"
SUTRA_TEXT = "व्यवहृपणोः समर्थयोः"
SUTRA_DESC = "(Samasa (compound formation)) — vyavahfpaRoH samarTayoH"


class Sutra2357:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

