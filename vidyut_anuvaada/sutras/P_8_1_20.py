# Sutra प.8.1.20: युष्मदस्मदोः षष्ठीचतुर्थीद्वितीयास्थयोर्वान्नावौ
# naścāpadāntasya ṅiḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.1.20"
SUTRA_TEXT = "युष्मदस्मदोः षष्ठीचतुर्थीद्वितीयास्थयोर्वान्नावौ"
SUTRA_DESC = "naścāpadāntasya ṅiḥ — repeated"


class Sutra8120:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.1.20: अग्निः'),
		('रामः', '', 'प.8.1.20: रामः'),
		('सीता', '', 'प.8.1.20: सीता'),
	]

