# Sutra प.5.3.22: सद्यःपरुत्परार्यैषमःपरेद्यव्यद्यपूर्वेद्युरन्येद्युरन्यतरेद्युरितरेद्युरपरेद्युरधरेद्युरुभयेद्युरुत्तरेद्युः
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — sadyaHparutparAryEzamaHparedyavyadyapUrvedyuranyedyuranyataredyuritaredyuraparedyuraDaredyuruBayedyuruttaredyuH

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.22"
SUTRA_TEXT = "सद्यःपरुत्परार्यैषमःपरेद्यव्यद्यपूर्वेद्युरन्येद्युरन्यतरेद्युरितरेद्युरपरेद्युरधरेद्युरुभयेद्युरुत्तरेद्युः"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — sadyaHparutparAryEzamaHparedyavyadyapUrvedyuranyedyuranyataredyuritaredyuraparedyuraDaredyuruBayedyuruttaredyuH"


class Sutra5322:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.22: अग्निः'),
		('रामः', '', 'प.5.3.22: रामः'),
		('सीता', '', 'प.5.3.22: सीता'),
	]

