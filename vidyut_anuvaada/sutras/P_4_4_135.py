# Sutra प.4.4.135: सहस्रेण संमितौ घः
# (Sup-sthāna (nominal endings) and kṛt-affixes) — sahasreRa saMmitO GaH

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.135"
SUTRA_TEXT = "सहस्रेण संमितौ घः"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — sahasreRa saMmitO GaH"


class Sutra44135:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.135: अग्निः'),
		('रामः', '', 'प.4.4.135: रामः'),
		('सीता', '', 'प.4.4.135: सीता'),
	]

