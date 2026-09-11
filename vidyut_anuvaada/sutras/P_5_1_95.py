# Sutra प.5.1.95: तस्य च दक्षिणा यज्ञाख्येभ्यः
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — tasya ca dakziRA yajYAKyeByaH

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.95"
SUTRA_TEXT = "तस्य च दक्षिणा यज्ञाख्येभ्यः"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — tasya ca dakziRA yajYAKyeByaH"


class Sutra5195:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.95: अग्निः'),
		('रामः', '', 'प.5.1.95: रामः'),
		('सीता', '', 'प.5.1.95: सीता'),
	]

