# Sutra प.3.1.58: जॄस्तम्भुम्रुचुम्लुचुग्रुचुग्लुचुग्लुञ्चुश्विभ्यश्च
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — jFstamBumrucumlucugrucuglucugluYcuSviByaSca

from P_3_1 import apply_3_1_58

SUTRA_CODE = "प.3.1.58"
SUTRA_TEXT = "जॄस्तम्भुम्रुचुम्लुचुग्रुचुग्लुचुग्लुञ्चुश्विभ्यश्च"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — jFstamBumrucumlucugrucuglucugluYcuSviByaSca"


class Sutra3158:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_58(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.58:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.58:root=रामः;pos='),
		('सीता', '', 'प.3.1.58:root=सीता;pos='),
	]

