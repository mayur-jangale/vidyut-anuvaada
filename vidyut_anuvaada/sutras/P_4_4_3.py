# Sutra प.4.4.3: संस्कृतम्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — saMskftam

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.3"
SUTRA_TEXT = "संस्कृतम्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — saMskftam"


class Sutra443:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.3: अग्निः'),
		('रामः', '', 'प.4.4.3: रामः'),
		('सीता', '', 'प.4.4.3: सीता'),
	]

