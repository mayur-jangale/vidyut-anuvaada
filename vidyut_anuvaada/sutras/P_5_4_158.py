# Sutra प.5.4.158: ऋतश्छन्दसि
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — ftaSCandasi

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.158"
SUTRA_TEXT = "ऋतश्छन्दसि"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — ftaSCandasi"


class Sutra54158:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.158: अग्निः'),
		('रामः', '', 'प.5.4.158: रामः'),
		('सीता', '', 'प.5.4.158: सीता'),
	]

