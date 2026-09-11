# Sutra प.6.3.99: अषष्ठ्यतृतीयास्थस्यान्यस्य दुगाशीराशाऽऽस्थाऽऽस्थितोत्सुकोतिकारकरागच्छेषु
# final-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.99"
SUTRA_TEXT = "अषष्ठ्यतृतीयास्थस्यान्यस्य दुगाशीराशाऽऽस्थाऽऽस्थितोत्सुकोतिकारकरागच्छेषु"
SUTRA_DESC = "final-sandhi — continued"


class Sutra6399:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.99: अग्निः'),
		('रामः', '', 'प.6.3.99: रामः'),
		('सीता', '', 'प.6.3.99: सीता'),
	]

