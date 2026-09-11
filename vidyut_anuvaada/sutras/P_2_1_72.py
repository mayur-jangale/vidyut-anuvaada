# Sutra प.2.1.72: मयूरव्यंसकादयश्च
# marker: mayūra-vyaṃsakādayaśca

from sutra_engines import apply_general

SUTRA_CODE = "प.2.1.72"
SUTRA_TEXT = "मयूरव्यंसकादयश्च"
SUTRA_DESC = "mayūra-vyaṃsakādayaśca"


class Sutra2172:
 def apply(self, word, pos):
  from P_2_1 import apply_2_1_72
  return apply_2_1_72(word, pos)


 EXAMPLES = [
	('अग्निः', '', 'प.2.1.72:mayūra-vyaṃsakādayaśca;input=अग्निः;pos='),
		('रामः', '', 'प.2.1.72:mayūra-vyaṃsakādayaśca;input=रामः;pos='),
		('सीता', '', 'प.2.1.72:mayūra-vyaṃsakādayaśca;input=सीता;pos='),
	]
