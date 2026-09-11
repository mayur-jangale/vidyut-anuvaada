# Sutra प.8.2.68: अहन्
# (Final transformations (tripāḍī)) — ahan

from sutra_engines import apply_general

SUTRA_CODE = "प.8.2.68"
SUTRA_TEXT = "अहन्"
SUTRA_DESC = "(Final transformations (tripāḍī)) — ahan"


class Sutra8268:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.2.68: अग्निः'),
		('रामः', '', 'प.8.2.68: रामः'),
		('सीता', '', 'प.8.2.68: सीता'),
	]

