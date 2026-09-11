# Sutra प.3.3.170: आवश्यकाधमर्ण्ययोर्णिनिः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — AvaSyakADamarRyayorRiniH

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.170"
SUTRA_TEXT = "आवश्यकाधमर्ण्ययोर्णिनिः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — AvaSyakADamarRyayorRiniH"


class Sutra33170:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

