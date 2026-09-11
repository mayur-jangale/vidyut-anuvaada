# Sutra प.8.3.119: निव्यभिभ्योऽड्व्यवाये वा छन्दसि
# (Final transformations (tripāḍī)) — nivyaBiByo'qvyavAye vA Candasi

from sutra_engines import apply_general

SUTRA_CODE = "प.8.3.119"
SUTRA_TEXT = "निव्यभिभ्योऽड्व्यवाये वा छन्दसि"
SUTRA_DESC = "(Final transformations (tripāḍī)) — nivyaBiByo'qvyavAye vA Candasi"


class Sutra83119:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.3.119: अग्निः'),
		('रामः', '', 'प.8.3.119: रामः'),
		('सीता', '', 'प.8.3.119: सीता'),
	]

