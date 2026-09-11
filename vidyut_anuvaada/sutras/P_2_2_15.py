# Sutra प.2.2.15: तृजकाभ्यां कर्तरि
# (Samasa (compound formation)) — tfjakAByAM kartari

from sutra_engines import apply_general

SUTRA_CODE = "प.2.2.15"
SUTRA_TEXT = "तृजकाभ्यां कर्तरि"
SUTRA_DESC = "(Samasa (compound formation)) — tfjakAByAM kartari"


class Sutra2215:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

