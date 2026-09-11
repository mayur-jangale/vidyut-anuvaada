# Sutra प.4.4.72: कठिनान्तप्रस्तारसंस्थानेषु व्यवहरति
# (Sup-sthāna (nominal endings) and kṛt-affixes) — kaWinAntaprastArasaMsTAnezu vyavaharati

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.72"
SUTRA_TEXT = "कठिनान्तप्रस्तारसंस्थानेषु व्यवहरति"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — kaWinAntaprastArasaMsTAnezu vyavaharati"


class Sutra4472:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.72: अग्निः'),
		('रामः', '', 'प.4.4.72: रामः'),
		('सीता', '', 'प.4.4.72: सीता'),
	]

