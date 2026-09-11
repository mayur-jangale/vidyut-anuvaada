# Sutra प.8.2.106: प्लुतावैच इदुतौ
# (Final transformations (tripāḍī)) — plutAvEca idutO

from sutra_engines import apply_general

SUTRA_CODE = "प.8.2.106"
SUTRA_TEXT = "प्लुतावैच इदुतौ"
SUTRA_DESC = "(Final transformations (tripāḍī)) — plutAvEca idutO"


class Sutra82106:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.2.106: अग्निः'),
		('रामः', '', 'प.8.2.106: रामः'),
		('सीता', '', 'प.8.2.106: सीता'),
	]

