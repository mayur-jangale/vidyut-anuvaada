# Sutra प.1.2.48: गोस्त्रियोरुपसर्जनस्य
# (Samjna (technical definitions)) — gostriyorupasarjanasya

from P_1_2 import apply_1_2_48

SUTRA_CODE = "प.1.2.48"
SUTRA_TEXT = "गोस्त्रियोरुपसर्जनस्य"
SUTRA_DESC = "(Samjna (technical definitions)) — gostriyorupasarjanasya"


class Sutra1248:
	def apply(self, word, pos):
		return apply_1_2_48(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'non-go-strī:अग्निः'),
		('रामः', '', 'non-go-strī:रामः'),
		('सीता', '', 'non-go-strī:सीता'),
	]

