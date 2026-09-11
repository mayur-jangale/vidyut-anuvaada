# Sutra प.5.2.73: अधिकम्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — aDikam

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.73"
SUTRA_TEXT = "अधिकम्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — aDikam"


class Sutra5273:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.73: अग्निः'),
		('रामः', '', 'प.5.2.73: रामः'),
		('सीता', '', 'प.5.2.73: सीता'),
	]

