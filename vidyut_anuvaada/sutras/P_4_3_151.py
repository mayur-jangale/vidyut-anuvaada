# Sutra प.4.3.151: नोत्वद्वर्ध्रबिल्वात्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — notvadvarDrabilvAt

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.151"
SUTRA_TEXT = "नोत्वद्वर्ध्रबिल्वात्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — notvadvarDrabilvAt"


class Sutra43151:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.151: अग्निः'),
		('रामः', '', 'प.4.3.151: रामः'),
		('सीता', '', 'प.4.3.151: सीता'),
	]

