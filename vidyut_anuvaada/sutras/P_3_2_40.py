# Sutra प.3.2.40: वाचि यमो व्रते
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — vAci yamo vrate

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.40"
SUTRA_TEXT = "वाचि यमो व्रते"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — vAci yamo vrate"


class Sutra3240:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

