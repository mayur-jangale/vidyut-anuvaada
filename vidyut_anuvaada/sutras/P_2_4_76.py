# Sutra प.2.4.76: बहुलं छन्दसि
# (Samasa (compound formation)) — bahulaM Candasi

from sutra_engines import apply_general

SUTRA_CODE = "प.2.4.76"
SUTRA_TEXT = "बहुलं छन्दसि"
SUTRA_DESC = "(Samasa (compound formation)) — bahulaM Candasi"


class Sutra2476:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

