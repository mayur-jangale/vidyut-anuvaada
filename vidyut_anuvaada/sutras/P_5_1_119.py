# Sutra प.5.1.119: तस्य भावस्त्वतलौ
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — tasya BAvastvatalO

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.119"
SUTRA_TEXT = "तस्य भावस्त्वतलौ"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — tasya BAvastvatalO"


class Sutra51119:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.119: अग्निः'),
		('रामः', '', 'प.5.1.119: रामः'),
		('सीता', '', 'प.5.1.119: सीता'),
	]

