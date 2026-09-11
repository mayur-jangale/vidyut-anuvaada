# Sutra प.1.1.51: उरण् रपरः
# (Samjna (technical definitions)) — uraR raparaH

from sutra_engines import apply_general

SUTRA_CODE = "प.1.1.51"
SUTRA_TEXT = "उरण् रपरः"
SUTRA_DESC = "(Samjna (technical definitions)) — uraR raparaH"


class Sutra1151:
	def apply(self, word, pos):
		from P_1_1 import apply_1_1_51
		return apply_1_1_51(word, pos)

	EXAMPLES = [
		('उरण्', '', 'प.1.1.51:uraṇ-raparaḥ;input=उरण्'),
		('अग्नि', '', 'प.1.1.51:uraṇ-raparaḥ;input=अग्नि'),
	]

