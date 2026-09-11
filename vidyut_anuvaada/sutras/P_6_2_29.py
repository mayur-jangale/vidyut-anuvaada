# Sutra प.6.2.29: इगन्तकालकपालभगालशरावेषु द्विगौ
# hal-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.29"
SUTRA_TEXT = "इगन्तकालकपालभगालशरावेषु द्विगौ"
SUTRA_DESC = "hal-sandhi — continued"


class Sutra6229:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.29: अग्निः'),
		('रामः', '', 'प.6.2.29: रामः'),
		('सीता', '', 'प.6.2.29: सीता'),
	]

