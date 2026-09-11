# Sutra प.6.2.171: वा जाते
# (Sandhi (euphonic combination)) — vA jAte

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.171"
SUTRA_TEXT = "वा जाते"
SUTRA_DESC = "(Sandhi (euphonic combination)) — vA jAte"


class Sutra62171:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.171: अग्निः'),
		('रामः', '', 'प.6.2.171: रामः'),
		('सीता', '', 'प.6.2.171: सीता'),
	]

