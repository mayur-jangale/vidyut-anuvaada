# Sutra प.1.4.25: भीत्रार्थानां भयहेतुः
# (Samjna (technical definitions)) — BItrArTAnAM BayahetuH

from sutra_engines import apply_general

SUTRA_CODE = "प.1.4.25"
SUTRA_TEXT = "भीत्रार्थानां भयहेतुः"
SUTRA_DESC = "(Samjna (technical definitions)) — BItrArTAnAM BayahetuH"


class Sutra1425:
	def apply(self, word, pos):
		from P_1_4 import apply_1_4_25
		return apply_1_4_25(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'not-apadana-bhayahetu:अग्निः'),
		('रामः', '', 'not-apadana-bhayahetu:रामः'),
		('सीता', '', 'not-apadana-bhayahetu:सीता'),
	]

