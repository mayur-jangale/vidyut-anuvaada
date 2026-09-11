# Sutra प.6.2.169: निष्ठोपमानादन्यतरस्याम्
# (Sandhi (euphonic combination)) — nizWopamAnAdanyatarasyAm

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.169"
SUTRA_TEXT = "निष्ठोपमानादन्यतरस्याम्"
SUTRA_DESC = "(Sandhi (euphonic combination)) — nizWopamAnAdanyatarasyAm"


class Sutra62169:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.169: अग्निः'),
		('रामः', '', 'प.6.2.169: रामः'),
		('सीता', '', 'प.6.2.169: सीता'),
	]

