# Sutra प.4.2.12: द्वैपवैयाघ्रादञ्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — dvEpavEyAGrAdaY

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.12"
SUTRA_TEXT = "द्वैपवैयाघ्रादञ्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — dvEpavEyAGrAdaY"


class Sutra4212:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.12: अग्निः'),
		('रामः', '', 'प.4.2.12: रामः'),
		('सीता', '', 'प.4.2.12: सीता'),
	]

