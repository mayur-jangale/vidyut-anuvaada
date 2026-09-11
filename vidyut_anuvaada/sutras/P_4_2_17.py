# Sutra प.4.2.17: शूलोखाद्यत्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — SUloKAdyat

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.17"
SUTRA_TEXT = "शूलोखाद्यत्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — SUloKAdyat"


class Sutra4217:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.17: अग्निः'),
		('रामः', '', 'प.4.2.17: रामः'),
		('सीता', '', 'प.4.2.17: सीता'),
	]

