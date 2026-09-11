# Sutra प.2.4.65: अत्रिभृगुकुत्सवसिष्ठगोतमाङ्गिरोभ्यश्च
# (Samasa (compound formation)) — atriBfgukutsavasizWagotamANgiroByaSca

from sutra_engines import apply_general

SUTRA_CODE = "प.2.4.65"
SUTRA_TEXT = "अत्रिभृगुकुत्सवसिष्ठगोतमाङ्गिरोभ्यश्च"
SUTRA_DESC = "(Samasa (compound formation)) — atriBfgukutsavasizWagotamANgiroByaSca"


class Sutra2465:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

