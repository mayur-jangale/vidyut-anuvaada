# Sutra प.4.3.88: शिशुक्रन्दयमसभद्वन्द्वेन्द्रजननादिभ्यश्छः
# (Sup-sthāna (nominal endings) and kṛt-affixes) — SiSukrandayamasaBadvandvendrajananAdiByaSCaH

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.88"
SUTRA_TEXT = "शिशुक्रन्दयमसभद्वन्द्वेन्द्रजननादिभ्यश्छः"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — SiSukrandayamasaBadvandvendrajananAdiByaSCaH"


class Sutra4388:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.88: अग्निः'),
		('रामः', '', 'प.4.3.88: रामः'),
		('सीता', '', 'प.4.3.88: सीता'),
	]

