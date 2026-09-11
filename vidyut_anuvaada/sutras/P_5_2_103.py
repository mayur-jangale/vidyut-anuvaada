# Sutra प.5.2.103: अण् च
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — aR ca

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.103"
SUTRA_TEXT = "अण् च"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — aR ca"


class Sutra52103:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.103: अग्निः'),
		('रामः', '', 'प.5.2.103: रामः'),
		('सीता', '', 'प.5.2.103: सीता'),
	]

