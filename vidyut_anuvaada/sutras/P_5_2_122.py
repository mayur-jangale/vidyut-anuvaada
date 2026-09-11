# Sutra प.5.2.122: बहुलं छन्दसि
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — bahulaM Candasi

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.122"
SUTRA_TEXT = "बहुलं छन्दसि"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — bahulaM Candasi"


class Sutra52122:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.122: अग्निः'),
		('रामः', '', 'प.5.2.122: रामः'),
		('सीता', '', 'प.5.2.122: सीता'),
	]

