# Sutra प.4.2.129: अरण्यान्मनुष्ये
# (Sup-sthāna (nominal endings) and kṛt-affixes) — araRyAnmanuzye

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.129"
SUTRA_TEXT = "अरण्यान्मनुष्ये"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — araRyAnmanuzye"


class Sutra42129:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.129: अग्निः'),
		('रामः', '', 'प.4.2.129: रामः'),
		('सीता', '', 'प.4.2.129: सीता'),
	]

