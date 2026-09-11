# Sutra प.2.1.44: संज्ञायाम्
# marker: saṃjñāyām

from sutra_engines import apply_general

SUTRA_CODE = "प.2.1.44"
SUTRA_TEXT = "संज्ञायाम्"
SUTRA_DESC = "saṃjñāyām"


class Sutra2144:
 def apply(self, word, pos):
  from P_2_1 import apply_2_1_44
  return apply_2_1_44(word, pos)


 EXAMPLES = [
	('अग्निः', '', 'प.2.1.44:saṃjñāyām;input=अग्निः;pos='),
		('रामः', '', 'प.2.1.44:saṃjñāyām;input=रामः;pos='),
		('सीता', '', 'प.2.1.44:saṃjñāyām;input=सीता;pos='),
	]
