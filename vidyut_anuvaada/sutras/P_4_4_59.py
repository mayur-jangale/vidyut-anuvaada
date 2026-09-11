# Sutra प.4.4.59: शक्तियष्ट्योरीकक्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — SaktiyazwyorIkak

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.59"
SUTRA_TEXT = "शक्तियष्ट्योरीकक्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — SaktiyazwyorIkak"


class Sutra4459:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.59: अग्निः'),
		('रामः', '', 'प.4.4.59: रामः'),
		('सीता', '', 'प.4.4.59: सीता'),
	]

