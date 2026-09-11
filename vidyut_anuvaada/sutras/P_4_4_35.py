# Sutra प.4.4.35: पक्षिमत्स्यमृगान् हन्ति
# (Sup-sthāna (nominal endings) and kṛt-affixes) — pakzimatsyamfgAn hanti

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.35"
SUTRA_TEXT = "पक्षिमत्स्यमृगान् हन्ति"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — pakzimatsyamfgAn hanti"


class Sutra4435:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.35: अग्निः'),
		('रामः', '', 'प.4.4.35: रामः'),
		('सीता', '', 'प.4.4.35: सीता'),
	]

