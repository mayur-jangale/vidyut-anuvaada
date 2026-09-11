# Sutra प.2.1.9: सुप्प्रतिना मात्रार्थे
# marker: su-amount

from sutra_engines import apply_general

SUTRA_CODE = "प.2.1.9"
SUTRA_TEXT = "सुप्प्रतिना मात्रार्थे"
SUTRA_DESC = "su-amount"


class Sutra219:
 def apply(self, word, pos):
  from P_2_1 import apply_2_1_9
  return apply_2_1_9(word, pos)


 EXAMPLES = [
	('अग्निः', '', 'प.2.1.9:su-amount;input=अग्निः;pos='),
		('रामः', '', 'प.2.1.9:su-amount;input=रामः;pos='),
		('सीता', '', 'प.2.1.9:su-amount;input=सीता;pos='),
	]
