# Sutra प.4.3.102: तित्तिरिवरतन्तुखण्डिकोखाच्छण्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — tittirivaratantuKaRqikoKAcCaR

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.102"
SUTRA_TEXT = "तित्तिरिवरतन्तुखण्डिकोखाच्छण्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — tittirivaratantuKaRqikoKAcCaR"


class Sutra43102:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.102: अग्निः'),
		('रामः', '', 'प.4.3.102: रामः'),
		('सीता', '', 'प.4.3.102: सीता'),
	]

