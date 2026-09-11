# Sutra प.4.3.143: मयड्वैतयोर्भाषायामभक्ष्याच्छादनयोः
# (Sup-sthāna (nominal endings) and kṛt-affixes) — mayaqvEtayorBAzAyAmaBakzyAcCAdanayoH

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.143"
SUTRA_TEXT = "मयड्वैतयोर्भाषायामभक्ष्याच्छादनयोः"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — mayaqvEtayorBAzAyAmaBakzyAcCAdanayoH"


class Sutra43143:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.143: अग्निः'),
		('रामः', '', 'प.4.3.143: रामः'),
		('सीता', '', 'प.4.3.143: सीता'),
	]

