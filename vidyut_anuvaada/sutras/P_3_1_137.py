# Sutra प.3.1.137: पाघ्राध्माधेट्दृशः शः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — pAGrADmADewdfSaH SaH

from P_3_1 import apply_3_1_137

SUTRA_CODE = "प.3.1.137"
SUTRA_TEXT = "पाघ्राध्माधेट्दृशः शः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — pAGrADmADewdfSaH SaH"


class Sutra31137:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_137(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.137:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.137:root=रामः;pos='),
		('सीता', '', 'प.3.1.137:root=सीता;pos='),
	]

