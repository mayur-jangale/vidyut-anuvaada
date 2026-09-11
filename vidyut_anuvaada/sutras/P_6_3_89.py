# Sutra प.6.3.89: दृग्दृशवतुषु
# final-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.89"
SUTRA_TEXT = "दृग्दृशवतुषु"
SUTRA_DESC = "final-sandhi — continued"


class Sutra6389:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.89: अग्निः'),
		('रामः', '', 'प.6.3.89: रामः'),
		('सीता', '', 'प.6.3.89: सीता'),
	]

