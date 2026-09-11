# Sutra प.6.2.50: तादौ च निति कृत्यतौ
# hal-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.50"
SUTRA_TEXT = "तादौ च निति कृत्यतौ"
SUTRA_DESC = "hal-sandhi — continued"


class Sutra6250:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.50: अग्निः'),
		('रामः', '', 'प.6.2.50: रामः'),
		('सीता', '', 'प.6.2.50: सीता'),
	]

