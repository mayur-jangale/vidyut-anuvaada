# Sutra प.7.4.37: अश्वाघस्यात्
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.7.4.37"
SUTRA_TEXT = "अश्वाघस्यात्"
SUTRA_DESC = "taddhita — continued"


class Sutra7437:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.4.37: अग्निः'),
		('रामः', '', 'प.7.4.37: रामः'),
		('सीता', '', 'प.7.4.37: सीता'),
	]

