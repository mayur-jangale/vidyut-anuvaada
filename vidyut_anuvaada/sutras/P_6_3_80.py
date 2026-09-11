# Sutra प.6.3.80: द्वितीये चानुपाख्ये
# final-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.80"
SUTRA_TEXT = "द्वितीये चानुपाख्ये"
SUTRA_DESC = "final-sandhi — continued"


class Sutra6380:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.80: अग्निः'),
		('रामः', '', 'प.6.3.80: रामः'),
		('सीता', '', 'प.6.3.80: सीता'),
	]

