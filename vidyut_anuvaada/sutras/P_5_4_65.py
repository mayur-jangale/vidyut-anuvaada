# Sutra प.5.4.65: शूलात् पाके
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — SUlAt pAke

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.65"
SUTRA_TEXT = "शूलात् पाके"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — SUlAt pAke"


class Sutra5465:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.65: अग्निः'),
		('रामः', '', 'प.5.4.65: रामः'),
		('सीता', '', 'प.5.4.65: सीता'),
	]

