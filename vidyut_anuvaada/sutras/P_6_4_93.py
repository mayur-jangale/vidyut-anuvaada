# Sutra प.6.4.93: चिण्णमुलोर्दीर्घोऽन्यतरस्याम्
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.93"
SUTRA_TEXT = "चिण्णमुलोर्दीर्घोऽन्यतरस्याम्"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra6493:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.93: अग्निः'),
		('रामः', '', 'प.6.4.93: रामः'),
		('सीता', '', 'प.6.4.93: सीता'),
	]

