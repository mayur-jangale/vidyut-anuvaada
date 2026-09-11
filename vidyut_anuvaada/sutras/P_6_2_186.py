# Sutra प.6.2.186: अपाच्च
# (Sandhi (euphonic combination)) — apAcca

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.186"
SUTRA_TEXT = "अपाच्च"
SUTRA_DESC = "(Sandhi (euphonic combination)) — apAcca"


class Sutra62186:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.186: अग्निः'),
		('रामः', '', 'प.6.2.186: रामः'),
		('सीता', '', 'प.6.2.186: सीता'),
	]

