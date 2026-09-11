# Sutra प.5.2.116: व्रीह्यादिभ्यश्च
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — vrIhyAdiByaSca

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.116"
SUTRA_TEXT = "व्रीह्यादिभ्यश्च"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — vrIhyAdiByaSca"


class Sutra52116:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.116: अग्निः'),
		('रामः', '', 'प.5.2.116: रामः'),
		('सीता', '', 'प.5.2.116: सीता'),
	]

