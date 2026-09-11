# Sutra प.3.3.135: नानद्यतनवत् क्रियाप्रबन्धसामीप्ययोः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — nAnadyatanavat kriyAprabanDasAmIpyayoH

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.135"
SUTRA_TEXT = "नानद्यतनवत् क्रियाप्रबन्धसामीप्ययोः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — nAnadyatanavat kriyAprabanDasAmIpyayoH"


class Sutra33135:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

