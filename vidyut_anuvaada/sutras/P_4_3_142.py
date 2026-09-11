# Sutra प.4.3.142: शम्याष्ट्लञ्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — SamyAzwlaY

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.142"
SUTRA_TEXT = "शम्याष्ट्लञ्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — SamyAzwlaY"


class Sutra43142:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.142: अग्निः'),
		('रामः', '', 'प.4.3.142: रामः'),
		('सीता', '', 'प.4.3.142: सीता'),
	]

