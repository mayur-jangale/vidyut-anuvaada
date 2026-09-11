# Sutra प.6.4.25: दंशसञ्जस्वञ्जां शपि
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.25"
SUTRA_TEXT = "दंशसञ्जस्वञ्जां शपि"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra6425:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.25: अग्निः'),
		('रामः', '', 'प.6.4.25: रामः'),
		('सीता', '', 'प.6.4.25: सीता'),
	]

