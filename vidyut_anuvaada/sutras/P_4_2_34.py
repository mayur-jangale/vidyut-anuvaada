# Sutra प.4.2.34: कालेभ्यो भववत्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — kAleByo Bavavat

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.34"
SUTRA_TEXT = "कालेभ्यो भववत्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — kAleByo Bavavat"


class Sutra4234:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.34: अग्निः'),
		('रामः', '', 'प.4.2.34: रामः'),
		('सीता', '', 'प.4.2.34: सीता'),
	]

