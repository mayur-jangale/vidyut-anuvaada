# Sutra प.2.4.14: न दधिपयआदीनि
# (Samasa (compound formation)) — na daDipayaAdIni

from sutra_engines import apply_general

SUTRA_CODE = "प.2.4.14"
SUTRA_TEXT = "न दधिपयआदीनि"
SUTRA_DESC = "(Samasa (compound formation)) — na daDipayaAdIni"


class Sutra2414:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

