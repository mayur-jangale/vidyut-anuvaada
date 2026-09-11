# Sutra प.7.3.33: आतो युक् चिण्कृतोः
# (Taddhita (secondary derivations)) — Ato yuk ciRkftoH

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.33"
SUTRA_TEXT = "आतो युक् चिण्कृतोः"
SUTRA_DESC = "(Taddhita (secondary derivations)) — Ato yuk ciRkftoH"


class Sutra7333:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.33: अग्निः'),
		('रामः', '', 'प.7.3.33: रामः'),
		('सीता', '', 'प.7.3.33: सीता'),
	]

