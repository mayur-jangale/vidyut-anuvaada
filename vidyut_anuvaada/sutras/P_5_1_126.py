# Sutra प.5.1.126: सख्युर्यः
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — saKyuryaH

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.126"
SUTRA_TEXT = "सख्युर्यः"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — saKyuryaH"


class Sutra51126:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.126: अग्निः'),
		('रामः', '', 'प.5.1.126: रामः'),
		('सीता', '', 'प.5.1.126: सीता'),
	]

