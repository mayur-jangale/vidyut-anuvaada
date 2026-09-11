# Sutra प.5.4.132: धनुषश्च
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — DanuzaSca

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.132"
SUTRA_TEXT = "धनुषश्च"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — DanuzaSca"


class Sutra54132:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.132: अग्निः'),
		('रामः', '', 'प.5.4.132: रामः'),
		('सीता', '', 'प.5.4.132: सीता'),
	]

