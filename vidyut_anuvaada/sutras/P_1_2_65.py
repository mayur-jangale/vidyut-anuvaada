# Sutra प.1.2.65: वृद्धो यूना तल्लक्षणश्चेदेव विशेषः
# (Samjna (technical definitions)) — vfdDo yUnA tallakzaRaScedeva viSezaH

from P_1_2 import apply_1_2_65

SUTRA_CODE = "प.1.2.65"
SUTRA_TEXT = "वृद्धो यूना तल्लक्षणश्चेदेव विशेषः"
SUTRA_DESC = "(Samjna (technical definitions)) — vfdDo yUnA tallakzaRaScedeva viSezaH"


class Sutra1265:
	def apply(self, word, pos):
		return apply_1_2_65(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'non-yūna-vṛddha:अग्निः'),
		('रामः', '', 'non-yūna-vṛddha:रामः'),
		('सीता', '', 'non-yūna-vṛddha:सीता'),
	]

