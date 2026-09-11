# Sutra प.6.3.54: हिमकाषिहतिषु च
# final-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.54"
SUTRA_TEXT = "हिमकाषिहतिषु च"
SUTRA_DESC = "final-sandhi — continued"


class Sutra6354:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.54: अग्निः'),
		('रामः', '', 'प.6.3.54: रामः'),
		('सीता', '', 'प.6.3.54: सीता'),
	]

