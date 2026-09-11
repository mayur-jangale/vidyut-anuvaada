# Sutra प.2.1.2: सुबामन्त्रिते पराङ्गवत् स्वरे
# marker: svarā-rule

from sutra_engines import apply_general

SUTRA_CODE = "प.2.1.2"
SUTRA_TEXT = "सुबामन्त्रिते पराङ्गवत् स्वरे"
SUTRA_DESC = "svarā-rule"


class Sutra212:
 def apply(self, word, pos):
  from P_2_1 import apply_2_1_2
  return apply_2_1_2(word, pos)


 EXAMPLES = [
	('अग्निः', '', 'प.2.1.2:svarā-rule;input=अग्निः;pos='),
		('रामः', '', 'प.2.1.2:svarā-rule;input=रामः;pos='),
		('सीता', '', 'प.2.1.2:svarā-rule;input=सीता;pos='),
	]
