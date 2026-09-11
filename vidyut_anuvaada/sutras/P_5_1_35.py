# Sutra प.5.1.35: शाणाद्वा
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — SARAdvA

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.35"
SUTRA_TEXT = "शाणाद्वा"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — SARAdvA"


class Sutra5135:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.35: अग्निः'),
		('रामः', '', 'प.5.1.35: रामः'),
		('सीता', '', 'प.5.1.35: सीता'),
	]

