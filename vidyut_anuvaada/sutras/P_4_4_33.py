# Sutra प.4.4.33: रक्षति
# (Sup-sthāna (nominal endings) and kṛt-affixes) — rakzati

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.33"
SUTRA_TEXT = "रक्षति"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — rakzati"


class Sutra4433:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.33: अग्निः'),
		('रामः', '', 'प.4.4.33: रामः'),
		('सीता', '', 'प.4.4.33: सीता'),
	]

