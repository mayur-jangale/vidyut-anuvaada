# Sutra प.1.4.36: स्पृहेरीप्सितः
# (Samjna (technical definitions)) — spfherIpsitaH

from sutra_engines import apply_general

SUTRA_CODE = "प.1.4.36"
SUTRA_TEXT = "स्पृहेरीप्सितः"
SUTRA_DESC = "(Samjna (technical definitions)) — spfherIpsitaH"


class Sutra1436:
	def apply(self, word, pos):
		from P_1_4 import apply_1_4_36
		return apply_1_4_36(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'not-spRhA-sampradAnam:अग्निः'),
		('रामः', '', 'not-spRhA-sampradAnam:रामः'),
		('सीता', '', 'not-spRhA-sampradAnam:सीता'),
	]

