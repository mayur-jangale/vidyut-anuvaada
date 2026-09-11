# Sutra प.1.2.35: उच्चैस्तरां वा वषट्कारः
# (Samjna (technical definitions)) — uccEstarAM vA vazawkAraH

from P_1_2 import apply_1_2_35

SUTRA_CODE = "प.1.2.35"
SUTRA_TEXT = "उच्चैस्तरां वा वषट्कारः"
SUTRA_DESC = "(Samjna (technical definitions)) — uccEstarAM vA vazawkAraH"


class Sutra1235:
	def apply(self, word, pos):
		return apply_1_2_35(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'non-vaṣaṭ:अग्निः'),
		('रामः', '', 'non-vaṣaṭ:रामः'),
		('सीता', '', 'non-vaṣaṭ:सीता'),
	]

