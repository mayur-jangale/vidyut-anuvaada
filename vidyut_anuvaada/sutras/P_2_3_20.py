# Sutra प.2.3.20: येनाङ्गविकारः
# (Samasa (compound formation)) — yenANgavikAraH

from sutra_engines import apply_general

SUTRA_CODE = "प.2.3.20"
SUTRA_TEXT = "येनाङ्गविकारः"
SUTRA_DESC = "(Samasa (compound formation)) — yenANgavikAraH"


class Sutra2320:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

