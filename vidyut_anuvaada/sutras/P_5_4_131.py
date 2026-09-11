# Sutra प.5.4.131: ऊधसोऽनङ्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — UDaso'naN

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.131"
SUTRA_TEXT = "ऊधसोऽनङ्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — UDaso'naN"


class Sutra54131:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.131: अग्निः'),
		('रामः', '', 'प.5.4.131: रामः'),
		('सीता', '', 'प.5.4.131: सीता'),
	]

