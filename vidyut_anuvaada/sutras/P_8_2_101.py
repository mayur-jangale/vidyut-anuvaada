# Sutra प.8.2.101: चिदिति चोपमाऽर्थे प्रयुज्यमाने
# (Final transformations (tripāḍī)) — ciditi copamA'rTe prayujyamAne

from sutra_engines import apply_general

SUTRA_CODE = "प.8.2.101"
SUTRA_TEXT = "चिदिति चोपमाऽर्थे प्रयुज्यमाने"
SUTRA_DESC = "(Final transformations (tripāḍī)) — ciditi copamA'rTe prayujyamAne"


class Sutra82101:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.2.101: अग्निः'),
		('रामः', '', 'प.8.2.101: रामः'),
		('सीता', '', 'प.8.2.101: सीता'),
	]

