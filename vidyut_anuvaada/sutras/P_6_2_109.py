# Sutra प.6.2.109: नदी बन्धुनि
# (Sandhi (euphonic combination)) — nadI banDuni

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.109"
SUTRA_TEXT = "नदी बन्धुनि"
SUTRA_DESC = "(Sandhi (euphonic combination)) — nadI banDuni"


class Sutra62109:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.109: अग्निः'),
		('रामः', '', 'प.6.2.109: रामः'),
		('सीता', '', 'प.6.2.109: सीता'),
	]

