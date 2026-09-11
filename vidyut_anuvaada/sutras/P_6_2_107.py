# Sutra प.6.2.107: उदराश्वेषुषु
# (Sandhi (euphonic combination)) — udarASvezuzu

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.107"
SUTRA_TEXT = "उदराश्वेषुषु"
SUTRA_DESC = "(Sandhi (euphonic combination)) — udarASvezuzu"


class Sutra62107:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.107: अग्निः'),
		('रामः', '', 'प.6.2.107: रामः'),
		('सीता', '', 'प.6.2.107: सीता'),
	]

