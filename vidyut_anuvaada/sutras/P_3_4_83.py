# Sutra प.3.4.83: विदो लटो वा
# leṭ — Vedic subjunctive endings

from sutra_engines import apply_general

SUTRA_CODE = "प.3.4.83"
SUTRA_TEXT = "विदो लटो वा"
SUTRA_DESC = "leṭ — Vedic subjunctive endings"


class Sutra3483:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

