# Sutra प.4.4.88: मूलमस्याबर्हि
# (Sup-sthāna (nominal endings) and kṛt-affixes) — mUlamasyAbarhi

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.88"
SUTRA_TEXT = "मूलमस्याबर्हि"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — mUlamasyAbarhi"


class Sutra4488:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.88: अग्निः'),
		('रामः', '', 'प.4.4.88: रामः'),
		('सीता', '', 'प.4.4.88: सीता'),
	]

