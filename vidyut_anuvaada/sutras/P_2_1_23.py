# Sutra प.2.1.23: द्विगुश्च
# marker: dviguśca

from sutra_engines import apply_general

SUTRA_CODE = "प.2.1.23"
SUTRA_TEXT = "द्विगुश्च"
SUTRA_DESC = "dviguśca"


class Sutra2123:
 def apply(self, word, pos):
  from P_2_1 import apply_2_1_23
  return apply_2_1_23(word, pos)


 EXAMPLES = [
	('अग्निः', '', 'प.2.1.23:dviguśca;input=अग्निः;pos='),
		('रामः', '', 'प.2.1.23:dviguśca;input=रामः;pos='),
		('सीता', '', 'प.2.1.23:dviguśca;input=सीता;pos='),
	]
