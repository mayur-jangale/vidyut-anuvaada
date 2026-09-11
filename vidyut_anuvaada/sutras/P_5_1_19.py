# Sutra प.5.1.19: आर्हादगोपुच्छसंख्यापरिमाणाट्ठक्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — ArhAdagopucCasaMKyAparimARAwWak

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.19"
SUTRA_TEXT = "आर्हादगोपुच्छसंख्यापरिमाणाट्ठक्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — ArhAdagopucCasaMKyAparimARAwWak"


class Sutra5119:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.19: अग्निः'),
		('रामः', '', 'प.5.1.19: रामः'),
		('सीता', '', 'प.5.1.19: सीता'),
	]

