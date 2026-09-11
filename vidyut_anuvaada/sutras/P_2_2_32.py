# Sutra प.2.2.32: द्वन्द्वे घि
# (Samasa (compound formation)) — dvandve Gi

from sutra_engines import apply_general

SUTRA_CODE = "प.2.2.32"
SUTRA_TEXT = "द्वन्द्वे घि"
SUTRA_DESC = "(Samasa (compound formation)) — dvandve Gi"


class Sutra2232:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

