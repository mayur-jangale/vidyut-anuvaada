# Sutra प.5.2.50: थट् चच्छन्दसि
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — Taw cacCandasi

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.50"
SUTRA_TEXT = "थट् चच्छन्दसि"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — Taw cacCandasi"


class Sutra5250:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.50: अग्निः'),
		('रामः', '', 'प.5.2.50: रामः'),
		('सीता', '', 'प.5.2.50: सीता'),
	]

