# Sutra प.3.4.44: ऊर्ध्वे शुषिपूरोः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — UrDve SuzipUroH

from sutra_engines import apply_general

SUTRA_CODE = "प.3.4.44"
SUTRA_TEXT = "ऊर्ध्वे शुषिपूरोः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — UrDve SuzipUroH"


class Sutra3444:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

