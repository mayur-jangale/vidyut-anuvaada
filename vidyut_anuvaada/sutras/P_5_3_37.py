# Sutra प.5.3.37: आहि च दूरे
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — Ahi ca dUre

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.37"
SUTRA_TEXT = "आहि च दूरे"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — Ahi ca dUre"


class Sutra5337:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.37: अग्निः'),
		('रामः', '', 'प.5.3.37: रामः'),
		('सीता', '', 'प.5.3.37: सीता'),
	]

