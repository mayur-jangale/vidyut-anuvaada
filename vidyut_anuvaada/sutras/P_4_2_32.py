# Sutra प.4.2.32: द्यावापृथिवीशुनासीरमरुत्वदग्नीषोमवास्तोष्पतिगृहमेधाच्छ च
# (Sup-sthāna (nominal endings) and kṛt-affixes) — dyAvApfTivISunAsIramarutvadagnIzomavAstozpatigfhameDAcCa ca

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.32"
SUTRA_TEXT = "द्यावापृथिवीशुनासीरमरुत्वदग्नीषोमवास्तोष्पतिगृहमेधाच्छ च"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — dyAvApfTivISunAsIramarutvadagnIzomavAstozpatigfhameDAcCa ca"


class Sutra4232:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.32: अग्निः'),
		('रामः', '', 'प.4.2.32: रामः'),
		('सीता', '', 'प.4.2.32: सीता'),
	]

