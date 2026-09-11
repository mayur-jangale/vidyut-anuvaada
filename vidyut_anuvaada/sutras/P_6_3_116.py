# Sutra प.6.3.116: नहिवृतिवृषिव्यधिरुचिसहितनिषु क्वौ
# final-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.116"
SUTRA_TEXT = "नहिवृतिवृषिव्यधिरुचिसहितनिषु क्वौ"
SUTRA_DESC = "final-sandhi — continued"


class Sutra63116:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.116: अग्निः'),
		('रामः', '', 'प.6.3.116: रामः'),
		('सीता', '', 'प.6.3.116: सीता'),
	]

