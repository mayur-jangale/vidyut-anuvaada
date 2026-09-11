# Sutra प.8.2.62: क्विन्प्रत्ययस्य कुः
# (Final transformations (tripāḍī)) — kvinpratyayasya kuH

from sutra_engines import apply_general

SUTRA_CODE = "प.8.2.62"
SUTRA_TEXT = "क्विन्प्रत्ययस्य कुः"
SUTRA_DESC = "(Final transformations (tripāḍī)) — kvinpratyayasya kuH"


class Sutra8262:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.2.62: अग्निः'),
		('रामः', '', 'प.8.2.62: रामः'),
		('सीता', '', 'प.8.2.62: सीता'),
	]

