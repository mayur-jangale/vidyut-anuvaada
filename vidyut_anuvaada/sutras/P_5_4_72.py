# Sutra प.5.4.72: पथो विभाषा
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — paTo viBAzA

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.72"
SUTRA_TEXT = "पथो विभाषा"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — paTo viBAzA"


class Sutra5472:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.72: अग्निः'),
		('रामः', '', 'प.5.4.72: रामः'),
		('सीता', '', 'प.5.4.72: सीता'),
	]

