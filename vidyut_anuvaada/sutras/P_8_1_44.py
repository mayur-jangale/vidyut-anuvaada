# Sutra प.8.1.44: किं क्रियाप्रश्नेऽनुपसर्गमप्रतिषिद्धम्
# naścāpadāntasya ṅiḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.1.44"
SUTRA_TEXT = "किं क्रियाप्रश्नेऽनुपसर्गमप्रतिषिद्धम्"
SUTRA_DESC = "naścāpadāntasya ṅiḥ — repeated"


class Sutra8144:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.1.44: अग्निः'),
		('रामः', '', 'प.8.1.44: रामः'),
		('सीता', '', 'प.8.1.44: सीता'),
	]

