# Sutra प.2.1.12: अपपरिबहिरञ्चवः पञ्चम्या
# marker: apa-pari-bahir-aṅcavah-pañcamī

from sutra_engines import apply_general

SUTRA_CODE = "प.2.1.12"
SUTRA_TEXT = "अपपरिबहिरञ्चवः पञ्चम्या"
SUTRA_DESC = "apa-pari-bahir-aṅcavah-pañcamī"


class Sutra2112:
 def apply(self, word, pos):
  from P_2_1 import apply_2_1_12
  return apply_2_1_12(word, pos)


 EXAMPLES = [
	('अग्निः', '', 'प.2.1.12:apa-pari-bahir-aṅcavah-pañcamī;input=अग्निः;pos='),
		('रामः', '', 'प.2.1.12:apa-pari-bahir-aṅcavah-pañcamī;input=रामः;pos='),
		('सीता', '', 'प.2.1.12:apa-pari-bahir-aṅcavah-pañcamī;input=सीता;pos='),
	]
