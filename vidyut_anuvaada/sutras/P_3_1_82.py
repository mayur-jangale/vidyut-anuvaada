# Sutra प.3.1.82: स्तन्भुस्तुन्भुस्कन्भुस्कुन्भुस्कुञ्भ्यः श्नुश्च
# ṅitvasya ca — specific treatment of ṅit suffixes

from P_3_1 import apply_3_1_82

SUTRA_CODE = "प.3.1.82"
SUTRA_TEXT = "स्तन्भुस्तुन्भुस्कन्भुस्कुन्भुस्कुञ्भ्यः श्नुश्च"
SUTRA_DESC = "ṅitvasya ca — specific treatment of ṅit suffixes"


class Sutra3182:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_82(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.82:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.82:root=रामः;pos='),
		('सीता', '', 'प.3.1.82:root=सीता;pos='),
	]

