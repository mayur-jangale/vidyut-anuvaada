# Sutra प.2.1.7: यथासादृश्ये
# marker: yathā-sādr̥śya

from sutra_engines import apply_general

SUTRA_CODE = "प.2.1.7"
SUTRA_TEXT = "यथासादृश्ये"
SUTRA_DESC = "yathā-sādr̥śya"


class Sutra217:
 def apply(self, word, pos):
  from P_2_1 import apply_2_1_7
  return apply_2_1_7(word, pos)


 EXAMPLES = [
	('अग्निः', '', 'प.2.1.7:yathā-sādr̥śya;input=अग्निः;pos='),
		('रामः', '', 'प.2.1.7:yathā-sādr̥śya;input=रामः;pos='),
		('सीता', '', 'प.2.1.7:yathā-sādr̥śya;input=सीता;pos='),
	]
