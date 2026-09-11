# Sutra प.6.2.106: बहुव्रीहौ विश्वं संज्ञायाम्
# (Sandhi (euphonic combination)) — bahuvrIhO viSvaM saMjYAyAm

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.106"
SUTRA_TEXT = "बहुव्रीहौ विश्वं संज्ञायाम्"
SUTRA_DESC = "(Sandhi (euphonic combination)) — bahuvrIhO viSvaM saMjYAyAm"


class Sutra62106:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.106: अग्निः'),
		('रामः', '', 'प.6.2.106: रामः'),
		('सीता', '', 'प.6.2.106: सीता'),
	]

