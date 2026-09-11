# Sutra प.2.1.21: अन्यपदार्थे च संज्ञायाम्
# marker: anyapadārthe-ca-saṃjñāyām

from sutra_engines import apply_general

SUTRA_CODE = "प.2.1.21"
SUTRA_TEXT = "अन्यपदार्थे च संज्ञायाम्"
SUTRA_DESC = "anyapadārthe-ca-saṃjñāyām"


class Sutra2121:
 def apply(self, word, pos):
  from P_2_1 import apply_2_1_21
  return apply_2_1_21(word, pos)


 EXAMPLES = [
	('अग्निः', '', 'प.2.1.21:anyapadārthe-ca-saṃjñāyām;input=अग्निः;pos='),
		('रामः', '', 'प.2.1.21:anyapadārthe-ca-saṃjñāyām;input=रामः;pos='),
		('सीता', '', 'प.2.1.21:anyapadārthe-ca-saṃjñāyām;input=सीता;pos='),
	]
