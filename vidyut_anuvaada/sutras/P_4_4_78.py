# Sutra प.4.4.78: खः सर्वधुरात्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — KaH sarvaDurAt

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.78"
SUTRA_TEXT = "खः सर्वधुरात्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — KaH sarvaDurAt"


class Sutra4478:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.78: अग्निः'),
		('रामः', '', 'प.4.4.78: रामः'),
		('सीता', '', 'प.4.4.78: सीता'),
	]

