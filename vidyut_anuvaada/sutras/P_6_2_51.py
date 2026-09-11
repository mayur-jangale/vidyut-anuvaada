# Sutra प.6.2.51: तवै चान्तश्च युगपत्
# hal-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.51"
SUTRA_TEXT = "तवै चान्तश्च युगपत्"
SUTRA_DESC = "hal-sandhi — continued"


class Sutra6251:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.51: अग्निः'),
		('रामः', '', 'प.6.2.51: रामः'),
		('सीता', '', 'प.6.2.51: सीता'),
	]

