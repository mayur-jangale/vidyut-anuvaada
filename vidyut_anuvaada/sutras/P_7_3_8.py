# Sutra प.7.3.8: श्वादेरिञि
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.8"
SUTRA_TEXT = "श्वादेरिञि"
SUTRA_DESC = "taddhita — continued"


class Sutra738:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.8: अग्निः'),
		('रामः', '', 'प.7.3.8: रामः'),
		('सीता', '', 'प.7.3.8: सीता'),
	]

