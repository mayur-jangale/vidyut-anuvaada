# Sutra प.1.4.20: अयस्मयादीनि च्छन्दसि
# (Samjna (technical definitions)) — ayasmayAdIni cCandasi

from sutra_engines import apply_general

SUTRA_CODE = "प.1.4.20"
SUTRA_TEXT = "अयस्मयादीनि च्छन्दसि"
SUTRA_DESC = "(Samjna (technical definitions)) — ayasmayAdIni cCandasi"


class Sutra1420:
	def apply(self, word, pos):
		from P_1_4 import apply_1_4_20
		return apply_1_4_20(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'not-vedic-adi:अग्निः'),
		('रामः', '', 'not-vedic-adi:रामः'),
		('सीता', '', 'not-vedic-adi:सीता'),
	]

