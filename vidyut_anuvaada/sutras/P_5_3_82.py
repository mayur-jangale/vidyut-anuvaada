# Sutra प.5.3.82: अजिनान्तस्योत्तरपदलोपश्च
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — ajinAntasyottarapadalopaSca

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.82"
SUTRA_TEXT = "अजिनान्तस्योत्तरपदलोपश्च"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — ajinAntasyottarapadalopaSca"


class Sutra5382:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.82: अग्निः'),
		('रामः', '', 'प.5.3.82: रामः'),
		('सीता', '', 'प.5.3.82: सीता'),
	]

