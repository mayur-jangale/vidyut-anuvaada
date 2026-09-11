# Sutra प.3.2.117: प्रश्ने चासन्नकाले
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — praSne cAsannakAle

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.117"
SUTRA_TEXT = "प्रश्ने चासन्नकाले"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — praSne cAsannakAle"


class Sutra32117:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

