# Sutra प.4.4.56: मड्डुकझर्झरादणन्यतरस्याम्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — maqqukaJarJarAdaRanyatarasyAm

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.56"
SUTRA_TEXT = "मड्डुकझर्झरादणन्यतरस्याम्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — maqqukaJarJarAdaRanyatarasyAm"


class Sutra4456:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.56: अग्निः'),
		('रामः', '', 'प.4.4.56: रामः'),
		('सीता', '', 'प.4.4.56: सीता'),
	]

