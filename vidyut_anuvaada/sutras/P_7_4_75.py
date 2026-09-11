# Sutra प.7.4.75: निजां त्रयाणां गुणः श्लौ
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.7.4.75"
SUTRA_TEXT = "निजां त्रयाणां गुणः श्लौ"
SUTRA_DESC = "taddhita — continued"


class Sutra7475:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.4.75: अग्निः'),
		('रामः', '', 'प.7.4.75: रामः'),
		('सीता', '', 'प.7.4.75: सीता'),
	]

