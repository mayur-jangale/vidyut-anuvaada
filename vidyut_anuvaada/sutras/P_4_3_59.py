# Sutra प.4.3.59: अव्ययीभावाच्च
# (Sup-sthāna (nominal endings) and kṛt-affixes) — avyayIBAvAcca

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.59"
SUTRA_TEXT = "अव्ययीभावाच्च"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — avyayIBAvAcca"


class Sutra4359:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.59: अग्निः'),
		('रामः', '', 'प.4.3.59: रामः'),
		('सीता', '', 'प.4.3.59: सीता'),
	]

