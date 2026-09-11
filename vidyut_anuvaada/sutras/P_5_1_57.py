# Sutra प.5.1.57: तदस्य परिमाणम्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — tadasya parimARam

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.57"
SUTRA_TEXT = "तदस्य परिमाणम्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — tadasya parimARam"


class Sutra5157:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.57: अग्निः'),
		('रामः', '', 'प.5.1.57: रामः'),
		('सीता', '', 'प.5.1.57: सीता'),
	]

