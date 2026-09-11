# Sutra प.3.3.58: ग्रहवृदृनिश्चिगमश्च
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — grahavfdfniScigamaSca

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.58"
SUTRA_TEXT = "ग्रहवृदृनिश्चिगमश्च"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — grahavfdfniScigamaSca"


class Sutra3358:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

