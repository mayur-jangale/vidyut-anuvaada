# Sutra प.1.2.47: ह्रस्वो नपुंसके प्रातिपदिकस्य
# (Samjna (technical definitions)) — hrasvo napuMsake prAtipadikasya

from P_1_2 import apply_1_2_47

SUTRA_CODE = "प.1.2.47"
SUTRA_TEXT = "ह्रस्वो नपुंसके प्रातिपदिकस्य"
SUTRA_DESC = "(Samjna (technical definitions)) — hrasvo napuMsake prAtipadikasya"


class Sutra1247:
	def apply(self, word, pos):
		return apply_1_2_47(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'non-hrasva:अग्निः'),
		('रामः', '', 'non-hrasva:रामः'),
		('सीता', '', 'non-hrasva:सीता'),
	]

