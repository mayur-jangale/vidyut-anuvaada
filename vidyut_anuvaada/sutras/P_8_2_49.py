# Sutra प.8.2.49: दिवोऽविजिगीषायाम्
# (Final transformations (tripāḍī)) — divo'vijigIzAyAm

from sutra_engines import apply_general

SUTRA_CODE = "प.8.2.49"
SUTRA_TEXT = "दिवोऽविजिगीषायाम्"
SUTRA_DESC = "(Final transformations (tripāḍī)) — divo'vijigIzAyAm"


class Sutra8249:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.2.49: अग्निः'),
		('रामः', '', 'प.8.2.49: रामः'),
		('सीता', '', 'प.8.2.49: सीता'),
	]

