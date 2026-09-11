# Sutra प.2.1.20: नदीभिश्च
# marker: nadībhīśca

from sutra_engines import apply_general

SUTRA_CODE = "प.2.1.20"
SUTRA_TEXT = "नदीभिश्च"
SUTRA_DESC = "nadībhīśca"


class Sutra2120:
 def apply(self, word, pos):
  from P_2_1 import apply_2_1_20
  return apply_2_1_20(word, pos)


 EXAMPLES = [
	('अग्निः', '', 'प.2.1.20:nadībhīśca;input=अग्निः;pos='),
		('रामः', '', 'प.2.1.20:nadībhīśca;input=रामः;pos='),
		('सीता', '', 'प.2.1.20:nadībhīśca;input=सीता;pos='),
	]
