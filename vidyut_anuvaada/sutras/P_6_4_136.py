# Sutra प.6.4.136: विभाषा ङिश्योः
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.136"
SUTRA_TEXT = "विभाषा ङिश्योः"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra64136:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.136: अग्निः'),
		('रामः', '', 'प.6.4.136: रामः'),
		('सीता', '', 'प.6.4.136: सीता'),
	]

