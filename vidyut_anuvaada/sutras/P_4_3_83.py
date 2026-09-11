# Sutra प.4.3.83: प्रभवति
# (Sup-sthāna (nominal endings) and kṛt-affixes) — praBavati

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.83"
SUTRA_TEXT = "प्रभवति"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — praBavati"


class Sutra4383:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.83: अग्निः'),
		('रामः', '', 'प.4.3.83: रामः'),
		('सीता', '', 'प.4.3.83: सीता'),
	]

