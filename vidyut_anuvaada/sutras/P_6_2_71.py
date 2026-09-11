# Sutra प.6.2.71: भक्ताख्यास्तदर्थेषु
# hal-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.71"
SUTRA_TEXT = "भक्ताख्यास्तदर्थेषु"
SUTRA_DESC = "hal-sandhi — continued"


class Sutra6271:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.71: अग्निः'),
		('रामः', '', 'प.6.2.71: रामः'),
		('सीता', '', 'प.6.2.71: सीता'),
	]

