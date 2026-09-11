# Sutra प.5.3.103: शाखादिभ्यो यत्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — SAKAdiByo yat

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.103"
SUTRA_TEXT = "शाखादिभ्यो यत्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — SAKAdiByo yat"


class Sutra53103:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.103: अग्निः'),
		('रामः', '', 'प.5.3.103: रामः'),
		('सीता', '', 'प.5.3.103: सीता'),
	]

