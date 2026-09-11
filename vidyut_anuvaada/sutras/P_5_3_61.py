# Sutra प.5.3.61: ज्य च
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — jya ca

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.61"
SUTRA_TEXT = "ज्य च"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — jya ca"


class Sutra5361:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.61: अग्निः'),
		('रामः', '', 'प.5.3.61: रामः'),
		('सीता', '', 'प.5.3.61: सीता'),
	]

