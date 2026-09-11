# Sutra प.3.3.9: लिङ् चोर्ध्वमौहूर्तिके
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — liN corDvamOhUrtike

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.9"
SUTRA_TEXT = "लिङ् चोर्ध्वमौहूर्तिके"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — liN corDvamOhUrtike"


class Sutra339:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

