# Sutra प.6.2.97: द्विगौ क्रतौ
# hal-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.97"
SUTRA_TEXT = "द्विगौ क्रतौ"
SUTRA_DESC = "hal-sandhi — continued"


class Sutra6297:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.97: अग्निः'),
		('रामः', '', 'प.6.2.97: रामः'),
		('सीता', '', 'प.6.2.97: सीता'),
	]

