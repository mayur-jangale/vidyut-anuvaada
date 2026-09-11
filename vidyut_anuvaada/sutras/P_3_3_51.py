# Sutra प.3.3.51: अवे ग्रहो वर्षप्रतिबन्धे
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — ave graho varzapratibanDe

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.51"
SUTRA_TEXT = "अवे ग्रहो वर्षप्रतिबन्धे"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — ave graho varzapratibanDe"


class Sutra3351:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

