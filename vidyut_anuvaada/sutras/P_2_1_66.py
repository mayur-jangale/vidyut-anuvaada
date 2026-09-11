# Sutra प.2.1.66: प्रशंसावचनैश्च
# marker: praśaṃsā-vacanaiśca

from sutra_engines import apply_general

SUTRA_CODE = "प.2.1.66"
SUTRA_TEXT = "प्रशंसावचनैश्च"
SUTRA_DESC = "praśaṃsā-vacanaiśca"


class Sutra2166:
 def apply(self, word, pos):
  from P_2_1 import apply_2_1_66
  return apply_2_1_66(word, pos)


 EXAMPLES = [
	('अग्निः', '', 'प.2.1.66:praśaṃsā-vacanaiśca;input=अग्निः;pos='),
		('रामः', '', 'प.2.1.66:praśaṃsā-vacanaiśca;input=रामः;pos='),
		('सीता', '', 'प.2.1.66:praśaṃsā-vacanaiśca;input=सीता;pos='),
	]
