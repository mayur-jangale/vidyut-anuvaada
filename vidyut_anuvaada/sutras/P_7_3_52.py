# Sutra प.7.3.52: चजोः कु घिण्ण्यतोः
# (Taddhita (secondary derivations)) — cajoH ku GiRRyatoH

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.52"
SUTRA_TEXT = "चजोः कु घिण्ण्यतोः"
SUTRA_DESC = "(Taddhita (secondary derivations)) — cajoH ku GiRRyatoH"


class Sutra7352:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.52: अग्निः'),
		('रामः', '', 'प.7.3.52: रामः'),
		('सीता', '', 'प.7.3.52: सीता'),
	]

