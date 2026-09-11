# Sutra प.6.4.42: जनसनखनां सञ्झलोः
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.42"
SUTRA_TEXT = "जनसनखनां सञ्झलोः"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra6442:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.42: अग्निः'),
		('रामः', '', 'प.6.4.42: रामः'),
		('सीता', '', 'प.6.4.42: सीता'),
	]

