# Sutra प.2.1.30: तृतीया तत्कृतार्थेन गुणवचनेन
# marker: tṛtīyā-tatkṛtārthena-guṇavacanena

from sutra_engines import apply_general

SUTRA_CODE = "प.2.1.30"
SUTRA_TEXT = "तृतीया तत्कृतार्थेन गुणवचनेन"
SUTRA_DESC = "tṛtīyā-tatkṛtārthena-guṇavacanena"


class Sutra2130:
 def apply(self, word, pos):
  from P_2_1 import apply_2_1_30
  return apply_2_1_30(word, pos)


 EXAMPLES = [
	('अग्निः', '', 'प.2.1.30:tṛtīyā-tatkṛtārthena-guṇavacanena;input=अग्निः;pos='),
		('रामः', '', 'प.2.1.30:tṛtīyā-tatkṛtārthena-guṇavacanena;input=रामः;pos='),
		('सीता', '', 'प.2.1.30:tṛtīyā-tatkṛtārthena-guṇavacanena;input=सीता;pos='),
	]
