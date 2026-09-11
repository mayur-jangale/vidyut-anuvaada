# Sutra प.4.3.110: पाराशर्यशिलालिभ्यां भिक्षुनटसूत्रयोः
# (Sup-sthāna (nominal endings) and kṛt-affixes) — pArASaryaSilAliByAM BikzunawasUtrayoH

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.110"
SUTRA_TEXT = "पाराशर्यशिलालिभ्यां भिक्षुनटसूत्रयोः"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — pArASaryaSilAliByAM BikzunawasUtrayoH"


class Sutra43110:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.110: अग्निः'),
		('रामः', '', 'प.4.3.110: रामः'),
		('सीता', '', 'प.4.3.110: सीता'),
	]

