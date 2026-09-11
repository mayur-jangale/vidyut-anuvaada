# Sutra प.1.4.66: कणेमनसी श्रद्धाप्रतीघाते
# (Samjna (technical definitions)) — kaRemanasI SradDApratIGAte

from sutra_engines import apply_general

SUTRA_CODE = "प.1.4.66"
SUTRA_TEXT = "कणेमनसी श्रद्धाप्रतीघाते"
SUTRA_DESC = "(Samjna (technical definitions)) — kaRemanasI SradDApratIGAte"


class Sutra1466:
	def apply(self, word, pos):
		from P_1_4 import apply_1_4_66
		return apply_1_4_66(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'not-kaRa-manas:अग्निः'),
		('रामः', '', 'not-kaRa-manas:रामः'),
		('सीता', '', 'not-kaRa-manas:सीता'),
	]

