# Sutra प.1.4.30: जनिकर्तुः प्रकृतिः
# (Samjna (technical definitions)) — janikartuH prakftiH

from sutra_engines import apply_general

SUTRA_CODE = "प.1.4.30"
SUTRA_TEXT = "जनिकर्तुः प्रकृतिः"
SUTRA_DESC = "(Samjna (technical definitions)) — janikartuH prakftiH"


class Sutra1430:
	def apply(self, word, pos):
		from P_1_4 import apply_1_4_30
		return apply_1_4_30(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'not-janikartA:अग्निः'),
		('रामः', '', 'not-janikartA:रामः'),
		('सीता', '', 'not-janikartA:सीता'),
	]

