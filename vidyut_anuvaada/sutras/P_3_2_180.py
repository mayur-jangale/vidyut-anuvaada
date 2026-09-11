# Sutra प.3.2.180: विप्रसम्भ्यो ड्वसंज्ञायाम्
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — viprasamByo qvasaMjYAyAm

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.180"
SUTRA_TEXT = "विप्रसम्भ्यो ड्वसंज्ञायाम्"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — viprasamByo qvasaMjYAyAm"


class Sutra32180:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

