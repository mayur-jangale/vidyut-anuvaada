# Sutra प.2.1.4: सह सुपा
# marker: saha-supā

from sutra_engines import apply_general

SUTRA_CODE = "प.2.1.4"
SUTRA_TEXT = "सह सुपा"
SUTRA_DESC = "saha-supā"


class Sutra214:
 def apply(self, word, pos):
  from P_2_1 import apply_2_1_4
  return apply_2_1_4(word, pos)


 EXAMPLES = [
	('अग्निः', '', 'प.2.1.4:saha-supā;input=अग्निः;pos='),
		('रामः', '', 'प.2.1.4:saha-supā;input=रामः;pos='),
		('सीता', '', 'प.2.1.4:saha-supā;input=सीता;pos='),
	]
