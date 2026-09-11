# Sutra प.3.2.175: स्थेशभासपिसकसो वरच्
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — sTeSaBAsapisakaso varac

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.175"
SUTRA_TEXT = "स्थेशभासपिसकसो वरच्"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — sTeSaBAsapisakaso varac"


class Sutra32175:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

