# Sutra प.3.2.65: कव्यपुरीषपुरीष्येषु ञ्युट्
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — kavyapurIzapurIzyezu Yyuw

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.65"
SUTRA_TEXT = "कव्यपुरीषपुरीष्येषु ञ्युट्"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — kavyapurIzapurIzyezu Yyuw"


class Sutra3265:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

