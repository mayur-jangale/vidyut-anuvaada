# Sutra प.5.4.38: प्रज्ञादिभ्यश्च
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — prajYAdiByaSca

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.38"
SUTRA_TEXT = "प्रज्ञादिभ्यश्च"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — prajYAdiByaSca"


class Sutra5438:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.38: अग्निः'),
		('रामः', '', 'प.5.4.38: रामः'),
		('सीता', '', 'प.5.4.38: सीता'),
	]

