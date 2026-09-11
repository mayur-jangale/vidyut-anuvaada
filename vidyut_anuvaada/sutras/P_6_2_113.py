# Sutra प.6.2.113: संज्ञौपम्ययोश्च
# (Sandhi (euphonic combination)) — saMjYOpamyayoSca

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.113"
SUTRA_TEXT = "संज्ञौपम्ययोश्च"
SUTRA_DESC = "(Sandhi (euphonic combination)) — saMjYOpamyayoSca"


class Sutra62113:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.113: अग्निः'),
		('रामः', '', 'प.6.2.113: रामः'),
		('सीता', '', 'प.6.2.113: सीता'),
	]

