# Sutra प.6.2.139: गतिकारकोपपदात् कृत्
# (Sandhi (euphonic combination)) — gatikArakopapadAt kft

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.139"
SUTRA_TEXT = "गतिकारकोपपदात् कृत्"
SUTRA_DESC = "(Sandhi (euphonic combination)) — gatikArakopapadAt kft"


class Sutra62139:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.139: अग्निः'),
		('रामः', '', 'प.6.2.139: रामः'),
		('सीता', '', 'प.6.2.139: सीता'),
	]

