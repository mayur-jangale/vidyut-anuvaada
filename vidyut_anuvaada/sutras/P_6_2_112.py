# Sutra प.6.2.112: कर्णो वर्णलक्षणात्
# (Sandhi (euphonic combination)) — karRo varRalakzaRAt

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.112"
SUTRA_TEXT = "कर्णो वर्णलक्षणात्"
SUTRA_DESC = "(Sandhi (euphonic combination)) — karRo varRalakzaRAt"


class Sutra62112:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.112: अग्निः'),
		('रामः', '', 'प.6.2.112: रामः'),
		('सीता', '', 'प.6.2.112: सीता'),
	]

