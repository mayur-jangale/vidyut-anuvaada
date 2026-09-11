# Sutra प.7.1.62: नेट्यलिटि रधेः
# (Taddhita (secondary derivations)) — newyaliwi raDeH

from sutra_engines import apply_general

SUTRA_CODE = "प.7.1.62"
SUTRA_TEXT = "नेट्यलिटि रधेः"
SUTRA_DESC = "(Taddhita (secondary derivations)) — newyaliwi raDeH"


class Sutra7162:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.1.62: अग्निः'),
		('रामः', '', 'प.7.1.62: रामः'),
		('सीता', '', 'प.7.1.62: सीता'),
	]

