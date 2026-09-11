# Sutra प.5.1.16: तदस्य तदस्मिन् स्यादिति
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — tadasya tadasmin syAditi

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.16"
SUTRA_TEXT = "तदस्य तदस्मिन् स्यादिति"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — tadasya tadasmin syAditi"


class Sutra5116:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.16: अग्निः'),
		('रामः', '', 'प.5.1.16: रामः'),
		('सीता', '', 'प.5.1.16: सीता'),
	]

