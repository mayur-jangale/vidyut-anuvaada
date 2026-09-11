# Sutra प.4.2.98: दक्षिणापश्चात्पुरसस्त्यक्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — dakziRApaScAtpurasastyak

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.98"
SUTRA_TEXT = "दक्षिणापश्चात्पुरसस्त्यक्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — dakziRApaScAtpurasastyak"


class Sutra4298:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.98: अग्निः'),
		('रामः', '', 'प.4.2.98: रामः'),
		('सीता', '', 'प.4.2.98: सीता'),
	]

