# Sutra प.2.4.41: वेञो वयिः
# (Samasa (compound formation)) — veYo vayiH

from sutra_engines import apply_general

SUTRA_CODE = "प.2.4.41"
SUTRA_TEXT = "वेञो वयिः"
SUTRA_DESC = "(Samasa (compound formation)) — veYo vayiH"


class Sutra2441:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

