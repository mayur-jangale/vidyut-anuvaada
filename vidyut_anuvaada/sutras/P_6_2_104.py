# Sutra प.6.2.104: आचार्योपसर्जनश्चान्तेवासिनि
# (Sandhi (euphonic combination)) — AcAryopasarjanaScAntevAsini

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.104"
SUTRA_TEXT = "आचार्योपसर्जनश्चान्तेवासिनि"
SUTRA_DESC = "(Sandhi (euphonic combination)) — AcAryopasarjanaScAntevAsini"


class Sutra62104:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.104: अग्निः'),
		('रामः', '', 'प.6.2.104: रामः'),
		('सीता', '', 'प.6.2.104: सीता'),
	]

