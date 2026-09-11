# Sutra प.4.4.6: गोपुच्छाट्ठञ्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — gopucCAwWaY

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.6"
SUTRA_TEXT = "गोपुच्छाट्ठञ्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — gopucCAwWaY"


class Sutra446:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.6: अग्निः'),
		('रामः', '', 'प.4.4.6: रामः'),
		('सीता', '', 'प.4.4.6: सीता'),
	]

