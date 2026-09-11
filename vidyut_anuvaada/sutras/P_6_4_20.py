# Sutra प.6.4.20: ज्वरत्वरस्रिव्यविमवामुपधायाश्च
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.20"
SUTRA_TEXT = "ज्वरत्वरस्रिव्यविमवामुपधायाश्च"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra6420:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.20: अग्निः'),
		('रामः', '', 'प.6.4.20: रामः'),
		('सीता', '', 'प.6.4.20: सीता'),
	]

