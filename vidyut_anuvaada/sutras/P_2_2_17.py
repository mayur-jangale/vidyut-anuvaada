# Sutra प.2.2.17: नित्यं क्रीडाजीविकयोः
# (Samasa (compound formation)) — nityaM krIqAjIvikayoH

from sutra_engines import apply_general

SUTRA_CODE = "प.2.2.17"
SUTRA_TEXT = "नित्यं क्रीडाजीविकयोः"
SUTRA_DESC = "(Samasa (compound formation)) — nityaM krIqAjIvikayoH"


class Sutra2217:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

