# Sutra प.6.3.130: मित्रे चर्षौ
# final-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.130"
SUTRA_TEXT = "मित्रे चर्षौ"
SUTRA_DESC = "final-sandhi — continued"


class Sutra63130:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.130: अग्निः'),
		('रामः', '', 'प.6.3.130: रामः'),
		('सीता', '', 'प.6.3.130: सीता'),
	]

