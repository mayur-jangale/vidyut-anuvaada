# Sutra प43: kartror naSivahoH
# kartror jIva puruZayoH

from sutra_engines import apply_general
from P_3_4 import apply_3_4_43

SUTRA_CODE = "प43"
SUTRA_TEXT = "kartror naSivahoH"
SUTRA_DESC = "kartror jIva puruZayoH"


class Sutra3443:
	def apply(self, word, pos):
		return apply_3_4_43(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'p34-043:kartror jIva puruZayoH;input=अग्निः;stem=अग्निः;ending=-;pos='),
		('रामः', '', 'p34-043:kartror jIva puruZayoH;input=रामः;stem=रामः;ending=-;pos='),
		('सीता', '', 'p34-043:kartror jIva puruZayoH;input=सीता;stem=सीता;ending=-;pos='),
	]

