# Sutra प.8.2.103: स्वरितमाम्रेडितेऽसूयासम्मतिकोपकुत्सनेषु
# (Final transformations (tripāḍī)) — svaritamAmreqite'sUyAsammatikopakutsanezu

from sutra_engines import apply_general

SUTRA_CODE = "प.8.2.103"
SUTRA_TEXT = "स्वरितमाम्रेडितेऽसूयासम्मतिकोपकुत्सनेषु"
SUTRA_DESC = "(Final transformations (tripāḍī)) — svaritamAmreqite'sUyAsammatikopakutsanezu"


class Sutra82103:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.2.103: अग्निः'),
		('रामः', '', 'प.8.2.103: रामः'),
		('सीता', '', 'प.8.2.103: सीता'),
	]

