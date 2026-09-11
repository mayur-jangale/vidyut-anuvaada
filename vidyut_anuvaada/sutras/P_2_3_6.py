# Sutra प.2.3.6: अपवर्गे तृतीया
# (Samasa (compound formation)) — apavarge tftIyA

from sutra_engines import apply_general

SUTRA_CODE = "प.2.3.6"
SUTRA_TEXT = "अपवर्गे तृतीया"
SUTRA_DESC = "(Samasa (compound formation)) — apavarge tftIyA"


class Sutra236:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

