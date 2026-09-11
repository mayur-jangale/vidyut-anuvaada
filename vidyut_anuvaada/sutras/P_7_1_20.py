# Sutra प.7.1.20: जश्शसोः शिः
# (Taddhita (secondary derivations)) — jaSSasoH SiH

from sutra_engines import apply_general

SUTRA_CODE = "प.7.1.20"
SUTRA_TEXT = "जश्शसोः शिः"
SUTRA_DESC = "(Taddhita (secondary derivations)) — jaSSasoH SiH"


class Sutra7120:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.1.20: अग्निः'),
		('रामः', '', 'प.7.1.20: रामः'),
		('सीता', '', 'प.7.1.20: सीता'),
	]

