# Sutra प.5.4.123: बहुप्रजाश्छन्दसि
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — bahuprajASCandasi

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.123"
SUTRA_TEXT = "बहुप्रजाश्छन्दसि"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — bahuprajASCandasi"


class Sutra54123:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.123: अग्निः'),
		('रामः', '', 'प.5.4.123: रामः'),
		('सीता', '', 'प.5.4.123: सीता'),
	]

