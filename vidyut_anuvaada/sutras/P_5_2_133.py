# Sutra प.5.2.133: हस्ताज्जातौ
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — hastAjjAtO

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.133"
SUTRA_TEXT = "हस्ताज्जातौ"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — hastAjjAtO"


class Sutra52133:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.133: अग्निः'),
		('रामः', '', 'प.5.2.133: रामः'),
		('सीता', '', 'प.5.2.133: सीता'),
	]

