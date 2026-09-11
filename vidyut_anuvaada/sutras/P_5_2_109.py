# Sutra प.5.2.109: केशाद्वोऽन्यतरस्याम्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — keSAdvo'nyatarasyAm

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.109"
SUTRA_TEXT = "केशाद्वोऽन्यतरस्याम्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — keSAdvo'nyatarasyAm"


class Sutra52109:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.109: अग्निः'),
		('रामः', '', 'प.5.2.109: रामः'),
		('सीता', '', 'प.5.2.109: सीता'),
	]

