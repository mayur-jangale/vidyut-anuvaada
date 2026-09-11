# Sutra प.6.3.20: स्थे च भाषायाम्
# final-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.20"
SUTRA_TEXT = "स्थे च भाषायाम्"
SUTRA_DESC = "final-sandhi — continued"


class Sutra6320:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.20: अग्निः'),
		('रामः', '', 'प.6.3.20: रामः'),
		('सीता', '', 'प.6.3.20: सीता'),
	]

