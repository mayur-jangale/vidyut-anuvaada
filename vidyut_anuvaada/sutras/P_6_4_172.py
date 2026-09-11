# Sutra प.6.4.172: कार्मस्ताच्छील्ये
# (Sandhi (euphonic combination)) — kArmastAcCIlye

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.172"
SUTRA_TEXT = "कार्मस्ताच्छील्ये"
SUTRA_DESC = "(Sandhi (euphonic combination)) — kArmastAcCIlye"


class Sutra64172:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.172: अग्निः'),
		('रामः', '', 'प.6.4.172: रामः'),
		('सीता', '', 'प.6.4.172: सीता'),
	]

