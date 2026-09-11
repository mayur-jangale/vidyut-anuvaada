# Sutra प.7.2.115: अचो ञ्णिति
# (Taddhita (secondary derivations)) — aco YRiti

from sutra_engines import apply_general

SUTRA_CODE = "प.7.2.115"
SUTRA_TEXT = "अचो ञ्णिति"
SUTRA_DESC = "(Taddhita (secondary derivations)) — aco YRiti"


class Sutra72115:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.2.115: अग्निः'),
		('रामः', '', 'प.7.2.115: रामः'),
		('सीता', '', 'प.7.2.115: सीता'),
	]

