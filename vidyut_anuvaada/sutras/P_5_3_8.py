# Sutra प.5.3.8: तसेश्च
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — taseSca

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.8"
SUTRA_TEXT = "तसेश्च"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — taseSca"


class Sutra538:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.8: अग्निः'),
		('रामः', '', 'प.5.3.8: रामः'),
		('सीता', '', 'प.5.3.8: सीता'),
	]

