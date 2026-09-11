# Sutra प.6.3.127: चितेः कपि
# final-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.127"
SUTRA_TEXT = "चितेः कपि"
SUTRA_DESC = "final-sandhi — continued"


class Sutra63127:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.127: अग्निः'),
		('रामः', '', 'प.6.3.127: रामः'),
		('सीता', '', 'प.6.3.127: सीता'),
	]

