# Sutra प.2.1.8: यावदवधारणे
# marker: yāvat-avadhāraṇa

from sutra_engines import apply_general

SUTRA_CODE = "प.2.1.8"
SUTRA_TEXT = "यावदवधारणे"
SUTRA_DESC = "yāvat-avadhāraṇa"


class Sutra218:
 def apply(self, word, pos):
  from P_2_1 import apply_2_1_8
  return apply_2_1_8(word, pos)


 EXAMPLES = [
	('अग्निः', '', 'प.2.1.8:yāvat-avadhāraṇa;input=अग्निः;pos='),
		('रामः', '', 'प.2.1.8:yāvat-avadhāraṇa;input=रामः;pos='),
		('सीता', '', 'प.2.1.8:yāvat-avadhāraṇa;input=सीता;pos='),
	]
