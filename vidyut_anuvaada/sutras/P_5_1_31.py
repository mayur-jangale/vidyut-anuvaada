# Sutra प.5.1.31: बिस्ताच्च
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — bistAcca

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.31"
SUTRA_TEXT = "बिस्ताच्च"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — bistAcca"


class Sutra5131:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.31: अग्निः'),
		('रामः', '', 'प.5.1.31: रामः'),
		('सीता', '', 'प.5.1.31: सीता'),
	]

