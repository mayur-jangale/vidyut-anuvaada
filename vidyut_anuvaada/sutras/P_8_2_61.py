# Sutra प.8.2.61: नसत्तनिषत्तानुत्तप्रतूर्तसूर्तगूर्तानि छन्दसि
# (Final transformations (tripāḍī)) — nasattanizattAnuttapratUrtasUrtagUrtAni Candasi

from sutra_engines import apply_general

SUTRA_CODE = "प.8.2.61"
SUTRA_TEXT = "नसत्तनिषत्तानुत्तप्रतूर्तसूर्तगूर्तानि छन्दसि"
SUTRA_DESC = "(Final transformations (tripāḍī)) — nasattanizattAnuttapratUrtasUrtagUrtAni Candasi"


class Sutra8261:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.2.61: अग्निः'),
		('रामः', '', 'प.8.2.61: रामः'),
		('सीता', '', 'प.8.2.61: सीता'),
	]

