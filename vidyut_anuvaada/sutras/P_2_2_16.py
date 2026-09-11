# Sutra प.2.2.16: कर्तरि  च
# (Samasa (compound formation)) — kartari  ca

from sutra_engines import apply_general

SUTRA_CODE = "प.2.2.16"
SUTRA_TEXT = "कर्तरि  च"
SUTRA_DESC = "(Samasa (compound formation)) — kartari  ca"


class Sutra2216:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

