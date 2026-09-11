# Sutra प.6.3.57: उदकस्योदः संज्ञायाम्
# final-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.57"
SUTRA_TEXT = "उदकस्योदः संज्ञायाम्"
SUTRA_DESC = "final-sandhi — continued"


class Sutra6357:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.57: अग्निः'),
		('रामः', '', 'प.6.3.57: रामः'),
		('सीता', '', 'प.6.3.57: सीता'),
	]

