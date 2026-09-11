# Sutra प.8.2.65: म्वोश्च
# (Final transformations (tripāḍī)) — mvoSca

from sutra_engines import apply_general

SUTRA_CODE = "प.8.2.65"
SUTRA_TEXT = "म्वोश्च"
SUTRA_DESC = "(Final transformations (tripāḍī)) — mvoSca"


class Sutra8265:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.2.65: अग्निः'),
		('रामः', '', 'प.8.2.65: रामः'),
		('सीता', '', 'प.8.2.65: सीता'),
	]

