# Sutra प.7.3.88: भूसुवोस्तिङि
# (Taddhita (secondary derivations)) — BUsuvostiNi

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.88"
SUTRA_TEXT = "भूसुवोस्तिङि"
SUTRA_DESC = "(Taddhita (secondary derivations)) — BUsuvostiNi"


class Sutra7388:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.88: अग्निः'),
		('रामः', '', 'प.7.3.88: रामः'),
		('सीता', '', 'प.7.3.88: सीता'),
	]

