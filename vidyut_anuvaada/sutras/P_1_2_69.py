# Sutra प.1.2.69: नपुंसकमनपुंसकेनैकवच्चास्यान्यतरस्याम्
# (Samjna (technical definitions)) — napuMsakamanapuMsakenEkavaccAsyAnyatarasyAm

from P_1_2 import apply_1_2_69

SUTRA_CODE = "प.1.2.69"
SUTRA_TEXT = "नपुंसकमनपुंसकेनैकवच्चास्यान्यतरस्याम्"
SUTRA_DESC = "(Samjna (technical definitions)) — napuMsakamanapuMsakenEkavaccAsyAnyatarasyAm"


class Sutra1269:
	def apply(self, word, pos):
		return apply_1_2_69(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'non-napuṃsaka:अग्निः'),
		('रामः', '', 'non-napuṃsaka:रामः'),
		('सीता', '', 'non-napuṃsaka:सीता'),
	]

