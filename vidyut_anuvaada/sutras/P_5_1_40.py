# Sutra प.5.1.40: पुत्राच्छ च
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — putrAcCa ca

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.40"
SUTRA_TEXT = "पुत्राच्छ च"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — putrAcCa ca"


class Sutra5140:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.40: अग्निः'),
		('रामः', '', 'प.5.1.40: रामः'),
		('सीता', '', 'प.5.1.40: सीता'),
	]

