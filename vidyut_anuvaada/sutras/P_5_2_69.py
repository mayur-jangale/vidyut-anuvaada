# Sutra प.5.2.69: अंशं हारी
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — aMSaM hArI

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.69"
SUTRA_TEXT = "अंशं हारी"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — aMSaM hArI"


class Sutra5269:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.69: अग्निः'),
		('रामः', '', 'प.5.2.69: रामः'),
		('सीता', '', 'प.5.2.69: सीता'),
	]

