# Sutra प.6.4.160: ज्यादादीयसः
# samprasāraṇa — final rule

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.160"
SUTRA_TEXT = "ज्यादादीयसः"
SUTRA_DESC = "samprasāraṇa — final rule"


class Sutra64160:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.160: अग्निः'),
		('रामः', '', 'प.6.4.160: रामः'),
		('सीता', '', 'प.6.4.160: सीता'),
	]

