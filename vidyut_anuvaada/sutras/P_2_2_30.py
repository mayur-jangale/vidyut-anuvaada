# Sutra प.2.2.30: उपसर्जनं पूर्वम्
# (Samasa (compound formation)) — upasarjanaM pUrvam

from sutra_engines import apply_general

SUTRA_CODE = "प.2.2.30"
SUTRA_TEXT = "उपसर्जनं पूर्वम्"
SUTRA_DESC = "(Samasa (compound formation)) — upasarjanaM pUrvam"


class Sutra2230:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

