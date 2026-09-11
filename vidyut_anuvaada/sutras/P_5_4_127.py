# Sutra प.5.4.127: इच् कर्मव्यतिहारे
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — ic karmavyatihAre

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.127"
SUTRA_TEXT = "इच् कर्मव्यतिहारे"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — ic karmavyatihAre"


class Sutra54127:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.127: अग्निः'),
		('रामः', '', 'प.5.4.127: रामः'),
		('सीता', '', 'प.5.4.127: सीता'),
	]

