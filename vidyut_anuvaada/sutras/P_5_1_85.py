# Sutra प.5.1.85: समायाः खः
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — samAyAH KaH

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.85"
SUTRA_TEXT = "समायाः खः"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — samAyAH KaH"


class Sutra5185:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.85: अग्निः'),
		('रामः', '', 'प.5.1.85: रामः'),
		('सीता', '', 'प.5.1.85: सीता'),
	]

