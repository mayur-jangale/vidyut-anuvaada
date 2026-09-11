# Sutra प.3.3.36: समि मुष्टौ
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — sami muzwO

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.36"
SUTRA_TEXT = "समि मुष्टौ"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — sami muzwO"


class Sutra3336:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

