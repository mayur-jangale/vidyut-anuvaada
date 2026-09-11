# Sutra प.4.3.66: तस्य व्याख्यान इति च व्याख्यातव्यनाम्नः
# (Sup-sthāna (nominal endings) and kṛt-affixes) — tasya vyAKyAna iti ca vyAKyAtavyanAmnaH

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.66"
SUTRA_TEXT = "तस्य व्याख्यान इति च व्याख्यातव्यनाम्नः"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — tasya vyAKyAna iti ca vyAKyAtavyanAmnaH"


class Sutra4366:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.66: अग्निः'),
		('रामः', '', 'प.4.3.66: रामः'),
		('सीता', '', 'प.4.3.66: सीता'),
	]

