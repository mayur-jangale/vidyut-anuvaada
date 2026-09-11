# Sutra प.2.1.27: सामि
# marker: sāmi

from sutra_engines import apply_general

SUTRA_CODE = "प.2.1.27"
SUTRA_TEXT = "सामि"
SUTRA_DESC = "sāmi"


class Sutra2127:
 def apply(self, word, pos):
  from P_2_1 import apply_2_1_27
  return apply_2_1_27(word, pos)


 EXAMPLES = [
	('अग्निः', '', 'प.2.1.27:sāmi;input=अग्निः;pos='),
		('रामः', '', 'प.2.1.27:sāmi;input=रामः;pos='),
		('सीता', '', 'प.2.1.27:sāmi;input=सीता;pos='),
	]
