# Sutra प.2.1.3: प्राक् कडारात् समासः
# marker: samāsa-before-kaḍāra

from sutra_engines import apply_general

SUTRA_CODE = "प.2.1.3"
SUTRA_TEXT = "प्राक् कडारात् समासः"
SUTRA_DESC = "samāsa-before-kaḍāra"


class Sutra213:
 def apply(self, word, pos):
  from P_2_1 import apply_2_1_3
  return apply_2_1_3(word, pos)


 EXAMPLES = [
	('अग्निः', '', 'प.2.1.3:samāsa-before-kaḍāra;input=अग्निः;pos='),
		('रामः', '', 'प.2.1.3:samāsa-before-kaḍāra;input=रामः;pos='),
		('सीता', '', 'प.2.1.3:samāsa-before-kaḍāra;input=सीता;pos='),
	]
