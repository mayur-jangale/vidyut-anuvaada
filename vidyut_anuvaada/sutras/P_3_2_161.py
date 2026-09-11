# Sutra प.3.2.161: भञ्जभासमिदो घुरच्
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — BaYjaBAsamido Gurac

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.161"
SUTRA_TEXT = "भञ्जभासमिदो घुरच्"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — BaYjaBAsamido Gurac"


class Sutra32161:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

