# Sutra प.1.3.9: तस्य लोपः
from P_1_3 import apply_1_3_9


class Sutra139:
	def apply(self, word, pos):
		return apply_1_3_9(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'tasya-lopah:अग्निः;stripped=अग्निः'),
		('रामः', '', 'tasya-lopah:रामः;stripped=रामः'),
		('सीता', '', 'tasya-lopah:सीता;stripped=सीता'),
	]
