# Sutra प.3.2.131: द्विषोऽमित्रे
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — dvizo'mitre

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.131"
SUTRA_TEXT = "द्विषोऽमित्रे"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — dvizo'mitre"


class Sutra32131:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

