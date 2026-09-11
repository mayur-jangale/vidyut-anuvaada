# Sutra प.7.2.71: अञ्जेः सिचि
# (Taddhita (secondary derivations)) — aYjeH sici

from sutra_engines import apply_general

SUTRA_CODE = "प.7.2.71"
SUTRA_TEXT = "अञ्जेः सिचि"
SUTRA_DESC = "(Taddhita (secondary derivations)) — aYjeH sici"


class Sutra7271:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.2.71: अग्निः'),
		('रामः', '', 'प.7.2.71: रामः'),
		('सीता', '', 'प.7.2.71: सीता'),
	]

