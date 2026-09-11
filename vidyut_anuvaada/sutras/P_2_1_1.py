# Sutra प.2.1.1: समर्थः पदविधिः
# marker: compound-eligible

from sutra_engines import apply_general

SUTRA_CODE = "प.2.1.1"
SUTRA_TEXT = "समर्थः पदविधिः"
SUTRA_DESC = "compound-eligible"


class Sutra211:
 def apply(self, word, pos):
  from P_2_1 import apply_2_1_1
  return apply_2_1_1(word, pos)


 EXAMPLES = [
	('अग्निः', '', 'प.2.1.1:compound-eligible;input=अग्निः;pos='),
		('रामः', '', 'प.2.1.1:compound-eligible;input=रामः;pos='),
		('सीता', '', 'प.2.1.1:compound-eligible;input=सीता;pos='),
	]
