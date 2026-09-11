# Sutra प.5.2.108: द्युद्रुभ्यां मः
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — dyudruByAM maH

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.108"
SUTRA_TEXT = "द्युद्रुभ्यां मः"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — dyudruByAM maH"


class Sutra52108:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.108: अग्निः'),
		('रामः', '', 'प.5.2.108: रामः'),
		('सीता', '', 'प.5.2.108: सीता'),
	]

