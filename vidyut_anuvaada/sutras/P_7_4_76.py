# Sutra प.7.4.76: भृञामित्
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.7.4.76"
SUTRA_TEXT = "भृञामित्"
SUTRA_DESC = "taddhita — continued"


class Sutra7476:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.4.76: अग्निः'),
		('रामः', '', 'प.7.4.76: रामः'),
		('सीता', '', 'प.7.4.76: सीता'),
	]

