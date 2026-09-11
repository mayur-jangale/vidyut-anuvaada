# Sutra प.4.3.158: उमोर्णयोर्वा
# (Sup-sthāna (nominal endings) and kṛt-affixes) — umorRayorvA

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.158"
SUTRA_TEXT = "उमोर्णयोर्वा"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — umorRayorvA"


class Sutra43158:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.158: अग्निः'),
		('रामः', '', 'प.4.3.158: रामः'),
		('सीता', '', 'प.4.3.158: सीता'),
	]

