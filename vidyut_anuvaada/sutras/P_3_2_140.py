# Sutra प.3.2.140: त्रसिगृधिधृषिक्षिपेः क्नुः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — trasigfDiDfzikzipeH knuH

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.140"
SUTRA_TEXT = "त्रसिगृधिधृषिक्षिपेः क्नुः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — trasigfDiDfzikzipeH knuH"


class Sutra32140:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

