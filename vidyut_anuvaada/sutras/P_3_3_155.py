# Sutra प.3.3.155: विभाषा धातौ सम्भावनवचनेऽयदि
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — viBAzA DAtO samBAvanavacane'yadi

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.155"
SUTRA_TEXT = "विभाषा धातौ सम्भावनवचनेऽयदि"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — viBAzA DAtO samBAvanavacane'yadi"


class Sutra33155:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

