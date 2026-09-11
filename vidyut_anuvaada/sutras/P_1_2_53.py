# Sutra प.1.2.53: तदशिष्यं संज्ञाप्रमाणत्वात्
# (Samjna (technical definitions)) — tadaSizyaM saMjYApramARatvAt

from P_1_2 import apply_1_2_53

SUTRA_CODE = "प.1.2.53"
SUTRA_TEXT = "तदशिष्यं संज्ञाप्रमाणत्वात्"
SUTRA_DESC = "(Samjna (technical definitions)) — tadaSizyaM saMjYApramARatvAt"


class Sutra1253:
	def apply(self, word, pos):
		return apply_1_2_53(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'saṃjñā-pramāṇa:अग्निः;no-further-teaching'),
		('रामः', '', 'saṃjñā-pramāṇa:रामः;no-further-teaching'),
		('सीता', '', 'saṃjñā-pramāṇa:सीता;no-further-teaching'),
	]

