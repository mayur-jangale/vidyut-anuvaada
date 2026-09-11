# Sutra प.3.1.6: मान्बधदान्शान्भ्यो दीर्घश्चाभ्यासस्य
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — mAnbaDadAnSAnByo dIrGaScAByAsasya

from P_3_1 import apply_3_1_6

SUTRA_CODE = "प.3.1.6"
SUTRA_TEXT = "मान्बधदान्शान्भ्यो दीर्घश्चाभ्यासस्य"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — mAnbaDadAnSAnByo dIrGaScAByAsasya"


class Sutra316:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_6(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.6:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.6:root=रामः;pos='),
		('सीता', '', 'प.3.1.6:root=सीता;pos='),
	]

