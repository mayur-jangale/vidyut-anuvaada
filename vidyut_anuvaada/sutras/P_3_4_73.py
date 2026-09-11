# Sutra प.3.4.73: दाशगोघ्नौ सम्प्रदाने
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — dASagoGnO sampradAne

from sutra_engines import apply_general

SUTRA_CODE = "प.3.4.73"
SUTRA_TEXT = "दाशगोघ्नौ सम्प्रदाने"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — dASagoGnO sampradAne"


class Sutra3473:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

