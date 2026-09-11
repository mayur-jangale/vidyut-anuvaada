# Sutra प.2.3.62: चतुर्थ्यर्थे बहुलं छन्दसि
# (Samasa (compound formation)) — caturTyarTe bahulaM Candasi

from sutra_engines import apply_general

SUTRA_CODE = "प.2.3.62"
SUTRA_TEXT = "चतुर्थ्यर्थे बहुलं छन्दसि"
SUTRA_DESC = "(Samasa (compound formation)) — caturTyarTe bahulaM Candasi"


class Sutra2362:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

