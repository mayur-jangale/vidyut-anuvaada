# Sutra प.7.2.24: अर्देः संनिविभ्यः
# (Taddhita (secondary derivations)) — ardeH saMniviByaH

from sutra_engines import apply_general

SUTRA_CODE = "प.7.2.24"
SUTRA_TEXT = "अर्देः संनिविभ्यः"
SUTRA_DESC = "(Taddhita (secondary derivations)) — ardeH saMniviByaH"


class Sutra7224:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.2.24: अग्निः'),
		('रामः', '', 'प.7.2.24: रामः'),
		('सीता', '', 'प.7.2.24: सीता'),
	]

