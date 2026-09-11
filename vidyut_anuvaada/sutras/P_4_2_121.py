# Sutra प.4.2.121: धन्वयोपधाद्वुञ्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — DanvayopaDAdvuY

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.121"
SUTRA_TEXT = "धन्वयोपधाद्वुञ्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — DanvayopaDAdvuY"


class Sutra42121:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.121: अग्निः'),
		('रामः', '', 'प.4.2.121: रामः'),
		('सीता', '', 'प.4.2.121: सीता'),
	]

