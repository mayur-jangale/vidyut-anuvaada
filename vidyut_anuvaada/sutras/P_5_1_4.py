# Sutra प.5.1.4: विभाषा हविरपूपादिभ्यः
# strīpratyaya — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.4"
SUTRA_TEXT = "विभाषा हविरपूपादिभ्यः"
SUTRA_DESC = "strīpratyaya — continued"


class Sutra514:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.4: अग्निः'),
		('रामः', '', 'प.5.1.4: रामः'),
		('सीता', '', 'प.5.1.4: सीता'),
	]

