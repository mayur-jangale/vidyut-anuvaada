# Sutra प.5.3.62: वृद्धस्य च
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — vfdDasya ca

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.62"
SUTRA_TEXT = "वृद्धस्य च"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — vfdDasya ca"


class Sutra5362:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.62: अग्निः'),
		('रामः', '', 'प.5.3.62: रामः'),
		('सीता', '', 'प.5.3.62: सीता'),
	]

