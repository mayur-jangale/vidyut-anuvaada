# Sutra प.4.2.57: तदस्यां प्रहरणमिति क्रीडायाम् णः
# (Sup-sthāna (nominal endings) and kṛt-affixes) — tadasyAM praharaRamiti krIqAyAm RaH

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.57"
SUTRA_TEXT = "तदस्यां प्रहरणमिति क्रीडायाम् णः"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — tadasyAM praharaRamiti krIqAyAm RaH"


class Sutra4257:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.57: अग्निः'),
		('रामः', '', 'प.4.2.57: रामः'),
		('सीता', '', 'प.4.2.57: सीता'),
	]

