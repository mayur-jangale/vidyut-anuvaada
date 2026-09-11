# Sutra प.5.4.142: छन्दसि च
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — Candasi ca

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.142"
SUTRA_TEXT = "छन्दसि च"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — Candasi ca"


class Sutra54142:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.142: अग्निः'),
		('रामः', '', 'प.5.4.142: रामः'),
		('सीता', '', 'प.5.4.142: सीता'),
	]

