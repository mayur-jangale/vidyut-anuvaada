# Sutra प.4.3.20: वसन्ताच्च
# (Sup-sthāna (nominal endings) and kṛt-affixes) — vasantAcca

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.20"
SUTRA_TEXT = "वसन्ताच्च"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — vasantAcca"


class Sutra4320:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.20: अग्निः'),
		('रामः', '', 'प.4.3.20: रामः'),
		('सीता', '', 'प.4.3.20: सीता'),
	]

