# Sutra प.6.4.73: छन्दस्यपि दृश्यते
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.73"
SUTRA_TEXT = "छन्दस्यपि दृश्यते"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra6473:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.73: अग्निः'),
		('रामः', '', 'प.6.4.73: रामः'),
		('सीता', '', 'प.6.4.73: सीता'),
	]

