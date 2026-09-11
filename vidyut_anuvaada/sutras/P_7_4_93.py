# Sutra प.7.4.93: सन्वल्लघुनि चङ्परेऽनग्लोपे
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.7.4.93"
SUTRA_TEXT = "सन्वल्लघुनि चङ्परेऽनग्लोपे"
SUTRA_DESC = "taddhita — continued"


class Sutra7493:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.4.93: अग्निः'),
		('रामः', '', 'प.7.4.93: रामः'),
		('सीता', '', 'प.7.4.93: सीता'),
	]

