# Sutra प.8.2.46: क्षियो दीर्घात्
# (Final transformations (tripāḍī)) — kziyo dIrGAt

from sutra_engines import apply_general

SUTRA_CODE = "प.8.2.46"
SUTRA_TEXT = "क्षियो दीर्घात्"
SUTRA_DESC = "(Final transformations (tripāḍī)) — kziyo dIrGAt"


class Sutra8246:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.2.46: अग्निः'),
		('रामः', '', 'प.8.2.46: रामः'),
		('सीता', '', 'प.8.2.46: सीता'),
	]

