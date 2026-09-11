# Sutra प.5.1.106: छन्दसि घस्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — Candasi Gas

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.106"
SUTRA_TEXT = "छन्दसि घस्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — Candasi Gas"


class Sutra51106:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.106: अग्निः'),
		('रामः', '', 'प.5.1.106: रामः'),
		('सीता', '', 'प.5.1.106: सीता'),
	]

