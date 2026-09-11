# Sutra प.4.4.53: किशरादिभ्यः ष्ठन्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — kiSarAdiByaH zWan

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.53"
SUTRA_TEXT = "किशरादिभ्यः ष्ठन्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — kiSarAdiByaH zWan"


class Sutra4453:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.53: अग्निः'),
		('रामः', '', 'प.4.4.53: रामः'),
		('सीता', '', 'प.4.4.53: सीता'),
	]

