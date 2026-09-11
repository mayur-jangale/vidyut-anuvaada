# Sutra प.2.4.43: लुङि च
# (Samasa (compound formation)) — luNi ca

from sutra_engines import apply_general

SUTRA_CODE = "प.2.4.43"
SUTRA_TEXT = "लुङि च"
SUTRA_DESC = "(Samasa (compound formation)) — luNi ca"


class Sutra2443:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

