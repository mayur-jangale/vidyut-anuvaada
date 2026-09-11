# Sutra प.2.4.84: तृतीयासप्तम्योर्बहुलम्
# (Samasa (compound formation)) — tftIyAsaptamyorbahulam

from sutra_engines import apply_general

SUTRA_CODE = "प.2.4.84"
SUTRA_TEXT = "तृतीयासप्तम्योर्बहुलम्"
SUTRA_DESC = "(Samasa (compound formation)) — tftIyAsaptamyorbahulam"


class Sutra2484:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

