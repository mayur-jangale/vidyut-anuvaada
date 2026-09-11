# Sutra प.3.4.39: हस्ते वर्त्तिग्रहोः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — haste varttigrahoH

from sutra_engines import apply_general

SUTRA_CODE = "प.3.4.39"
SUTRA_TEXT = "हस्ते वर्त्तिग्रहोः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — haste varttigrahoH"


class Sutra3439:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

