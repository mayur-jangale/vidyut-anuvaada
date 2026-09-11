# Sutra प.2.1.40: सप्तमी शौण्डैः
# marker: saptamī-śauṇḍaiḥ

from sutra_engines import apply_general

SUTRA_CODE = "प.2.1.40"
SUTRA_TEXT = "सप्तमी शौण्डैः"
SUTRA_DESC = "saptamī-śauṇḍaiḥ"


class Sutra2140:
 def apply(self, word, pos):
  from P_2_1 import apply_2_1_40
  return apply_2_1_40(word, pos)


 EXAMPLES = [
	('अग्निः', '', 'प.2.1.40:saptamī-śauṇḍaiḥ;input=अग्निः;pos='),
		('रामः', '', 'प.2.1.40:saptamī-śauṇḍaiḥ;input=रामः;pos='),
		('सीता', '', 'प.2.1.40:saptamī-śauṇḍaiḥ;input=सीता;pos='),
	]
