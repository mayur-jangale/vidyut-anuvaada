# Sutra प.6.3.107: कवं चोष्णे
# final-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.107"
SUTRA_TEXT = "कवं चोष्णे"
SUTRA_DESC = "final-sandhi — continued"


class Sutra63107:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.107: अग्निः'),
		('रामः', '', 'प.6.3.107: रामः'),
		('सीता', '', 'प.6.3.107: सीता'),
	]

