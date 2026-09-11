# Sutra प.4.3.18: वर्षाभ्यष्ठक्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — varzAByazWak

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.18"
SUTRA_TEXT = "वर्षाभ्यष्ठक्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — varzAByazWak"


class Sutra4318:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.18: अग्निः'),
		('रामः', '', 'प.4.3.18: रामः'),
		('सीता', '', 'प.4.3.18: सीता'),
	]

