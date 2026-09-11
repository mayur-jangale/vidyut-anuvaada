# Sutra प.1.4.37: क्रुधद्रुहेर्ष्याऽसूयार्थानां यं प्रति कोपः
# (Samjna (technical definitions)) — kruDadruherzyA'sUyArTAnAM yaM prati kopaH

from sutra_engines import apply_general

SUTRA_CODE = "प.1.4.37"
SUTRA_TEXT = "क्रुधद्रुहेर्ष्याऽसूयार्थानां यं प्रति कोपः"
SUTRA_DESC = "(Samjna (technical definitions)) — kruDadruherzyA'sUyArTAnAM yaM prati kopaH"


class Sutra1437:
	def apply(self, word, pos):
		from P_1_4 import apply_1_4_37
		return apply_1_4_37(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'not-emotion-sampradAnam:अग्निः'),
		('रामः', '', 'not-emotion-sampradAnam:रामः'),
		('सीता', '', 'not-emotion-sampradAnam:सीता'),
	]

