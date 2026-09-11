# Sutra प.7.1.69: विभाषा चिण्णमुलोः
# (Taddhita (secondary derivations)) — viBAzA ciRRamuloH

from sutra_engines import apply_general

SUTRA_CODE = "प.7.1.69"
SUTRA_TEXT = "विभाषा चिण्णमुलोः"
SUTRA_DESC = "(Taddhita (secondary derivations)) — viBAzA ciRRamuloH"


class Sutra7169:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.1.69: अग्निः'),
		('रामः', '', 'प.7.1.69: रामः'),
		('सीता', '', 'प.7.1.69: सीता'),
	]

