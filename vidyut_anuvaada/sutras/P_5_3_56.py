# Sutra प.5.3.56: तिङश्च
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — tiNaSca

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.56"
SUTRA_TEXT = "तिङश्च"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — tiNaSca"


class Sutra5356:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.56: अग्निः'),
		('रामः', '', 'प.5.3.56: रामः'),
		('सीता', '', 'प.5.3.56: सीता'),
	]

