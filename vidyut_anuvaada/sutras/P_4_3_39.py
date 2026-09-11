# Sutra प.4.3.39: प्रायभवः
# (Sup-sthāna (nominal endings) and kṛt-affixes) — prAyaBavaH

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.39"
SUTRA_TEXT = "प्रायभवः"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — prAyaBavaH"


class Sutra4339:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.39: अग्निः'),
		('रामः', '', 'प.4.3.39: रामः'),
		('सीता', '', 'प.4.3.39: सीता'),
	]

