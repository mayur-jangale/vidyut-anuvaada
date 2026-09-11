# Sutra प.3.2.168: सनाशंसभिक्ष उः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — sanASaMsaBikza uH

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.168"
SUTRA_TEXT = "सनाशंसभिक्ष उः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — sanASaMsaBikza uH"


class Sutra32168:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

