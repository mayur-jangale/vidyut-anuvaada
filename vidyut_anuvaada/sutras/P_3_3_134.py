# Sutra प.3.3.134: आशंसावचने लिङ्
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — ASaMsAvacane liN

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.134"
SUTRA_TEXT = "आशंसावचने लिङ्"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — ASaMsAvacane liN"


class Sutra33134:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

