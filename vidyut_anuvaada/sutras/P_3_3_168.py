# Sutra प.3.3.168: लिङ् यदि
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — liN yadi

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.168"
SUTRA_TEXT = "लिङ् यदि"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — liN yadi"


class Sutra33168:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

