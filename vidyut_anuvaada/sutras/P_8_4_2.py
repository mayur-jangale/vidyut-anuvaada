# Sutra प.8.4.2: अट्कुप्वाङ्नुम्व्यवायेऽपि
# final transformations — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.8.4.2"
SUTRA_TEXT = "अट्कुप्वाङ्नुम्व्यवायेऽपि"
SUTRA_DESC = "final transformations — continued"


class Sutra842:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.4.2: अग्निः'),
		('रामः', '', 'प.8.4.2: रामः'),
		('सीता', '', 'प.8.4.2: सीता'),
	]

