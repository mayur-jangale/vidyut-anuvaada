# Sutra प.5.3.59: तुश्छन्दसि
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — tuSCandasi

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.59"
SUTRA_TEXT = "तुश्छन्दसि"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — tuSCandasi"


class Sutra5359:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.59: अग्निः'),
		('रामः', '', 'प.5.3.59: रामः'),
		('सीता', '', 'प.5.3.59: सीता'),
	]

