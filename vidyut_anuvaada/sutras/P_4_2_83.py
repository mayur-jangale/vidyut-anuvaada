# Sutra प.4.2.83: शर्कराया वा
# (Sup-sthāna (nominal endings) and kṛt-affixes) — SarkarAyA vA

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.83"
SUTRA_TEXT = "शर्कराया वा"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — SarkarAyA vA"


class Sutra4283:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.83: अग्निः'),
		('रामः', '', 'प.4.2.83: रामः'),
		('सीता', '', 'प.4.2.83: सीता'),
	]

