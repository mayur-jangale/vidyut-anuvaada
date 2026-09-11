# Sutra प.5.2.7: तत्सर्वादेः पथ्यङ्गकर्मपत्रपात्रं व्याप्नोति
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.7"
SUTRA_TEXT = "तत्सर्वादेः पथ्यङ्गकर्मपत्रपात्रं व्याप्नोति"
SUTRA_DESC = "taddhita — continued"


class Sutra527:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.7: अग्निः'),
		('रामः', '', 'प.5.2.7: रामः'),
		('सीता', '', 'प.5.2.7: सीता'),
	]

