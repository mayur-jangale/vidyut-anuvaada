# Sutra प.6.2.188: अधेरुपरिस्थम्
# (Sandhi (euphonic combination)) — aDeruparisTam

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.188"
SUTRA_TEXT = "अधेरुपरिस्थम्"
SUTRA_DESC = "(Sandhi (euphonic combination)) — aDeruparisTam"


class Sutra62188:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.188: अग्निः'),
		('रामः', '', 'प.6.2.188: रामः'),
		('सीता', '', 'प.6.2.188: सीता'),
	]

