# Sutra प.5.3.25: किमश्च
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — kimaSca

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.25"
SUTRA_TEXT = "किमश्च"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — kimaSca"


class Sutra5325:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.25: अग्निः'),
		('रामः', '', 'प.5.3.25: रामः'),
		('सीता', '', 'प.5.3.25: सीता'),
	]

