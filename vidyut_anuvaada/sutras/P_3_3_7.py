# Sutra प.3.3.7: लिप्स्यमानसिद्धौ च
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — lipsyamAnasidDO ca

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.7"
SUTRA_TEXT = "लिप्स्यमानसिद्धौ च"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — lipsyamAnasidDO ca"


class Sutra337:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

