# Sutra प.2.1.69: वर्णो वर्णेन
# marker: varṇo-varṇena

from sutra_engines import apply_general

SUTRA_CODE = "प.2.1.69"
SUTRA_TEXT = "वर्णो वर्णेन"
SUTRA_DESC = "varṇo-varṇena"


class Sutra2169:
 def apply(self, word, pos):
  from P_2_1 import apply_2_1_69
  return apply_2_1_69(word, pos)


 EXAMPLES = [
	('अग्निः', '', 'प.2.1.69:varṇo-varṇena;input=अग्निः;pos='),
		('रामः', '', 'प.2.1.69:varṇo-varṇena;input=रामः;pos='),
		('सीता', '', 'प.2.1.69:varṇo-varṇena;input=सीता;pos='),
	]
