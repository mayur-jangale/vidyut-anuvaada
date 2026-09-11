# Sutra प.6.2.110: निष्ठोपसर्गपूर्वमन्यतरस्याम्
# (Sandhi (euphonic combination)) — nizWopasargapUrvamanyatarasyAm

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.110"
SUTRA_TEXT = "निष्ठोपसर्गपूर्वमन्यतरस्याम्"
SUTRA_DESC = "(Sandhi (euphonic combination)) — nizWopasargapUrvamanyatarasyAm"


class Sutra62110:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.110: अग्निः'),
		('रामः', '', 'प.6.2.110: रामः'),
		('सीता', '', 'प.6.2.110: सीता'),
	]

