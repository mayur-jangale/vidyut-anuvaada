# Sutra प.5.1.46: पात्रात् ष्ठन्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — pAtrAt zWan

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.46"
SUTRA_TEXT = "पात्रात् ष्ठन्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — pAtrAt zWan"


class Sutra5146:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.46: अग्निः'),
		('रामः', '', 'प.5.1.46: रामः'),
		('सीता', '', 'प.5.1.46: सीता'),
	]

