# Sutra प.3.3.98: व्रजयजोर्भावे क्यप्
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — vrajayajorBAve kyap

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.98"
SUTRA_TEXT = "व्रजयजोर्भावे क्यप्"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — vrajayajorBAve kyap"


class Sutra3398:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

