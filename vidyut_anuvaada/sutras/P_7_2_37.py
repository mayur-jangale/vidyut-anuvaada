# Sutra प.7.2.37: ग्रहोऽलिटि दीर्घः
# (Taddhita (secondary derivations)) — graho'liwi dIrGaH

from sutra_engines import apply_general

SUTRA_CODE = "प.7.2.37"
SUTRA_TEXT = "ग्रहोऽलिटि दीर्घः"
SUTRA_DESC = "(Taddhita (secondary derivations)) — graho'liwi dIrGaH"


class Sutra7237:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.2.37: अग्निः'),
		('रामः', '', 'प.7.2.37: रामः'),
		('सीता', '', 'प.7.2.37: सीता'),
	]

