# Sutra प.5.4.62: निष्कुलान्निष्कोषणे
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — nizkulAnnizkozaRe

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.62"
SUTRA_TEXT = "निष्कुलान्निष्कोषणे"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — nizkulAnnizkozaRe"


class Sutra5462:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.62: अग्निः'),
		('रामः', '', 'प.5.4.62: रामः'),
		('सीता', '', 'प.5.4.62: सीता'),
	]

