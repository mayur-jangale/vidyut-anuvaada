# Sutra प.6.2.47: अहीने द्वितीया
# hal-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.47"
SUTRA_TEXT = "अहीने द्वितीया"
SUTRA_DESC = "hal-sandhi — continued"


class Sutra6247:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.47: अग्निः'),
		('रामः', '', 'प.6.2.47: रामः'),
		('सीता', '', 'प.6.2.47: सीता'),
	]

