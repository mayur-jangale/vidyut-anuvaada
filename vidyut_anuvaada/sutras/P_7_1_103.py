# Sutra प.7.1.103: बहुलं छन्दसि
# (Taddhita (secondary derivations)) — bahulaM Candasi

from sutra_engines import apply_general

SUTRA_CODE = "प.7.1.103"
SUTRA_TEXT = "बहुलं छन्दसि"
SUTRA_DESC = "(Taddhita (secondary derivations)) — bahulaM Candasi"


class Sutra71103:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.1.103: अग्निः'),
		('रामः', '', 'प.7.1.103: रामः'),
		('सीता', '', 'प.7.1.103: सीता'),
	]

