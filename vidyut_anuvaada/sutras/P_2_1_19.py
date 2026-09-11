# Sutra प.2.1.19: संख्या वंश्येन
# marker: saṃkhyā-vaṃśyena

from sutra_engines import apply_general

SUTRA_CODE = "प.2.1.19"
SUTRA_TEXT = "संख्या वंश्येन"
SUTRA_DESC = "saṃkhyā-vaṃśyena"


class Sutra2119:
 def apply(self, word, pos):
  from P_2_1 import apply_2_1_19
  return apply_2_1_19(word, pos)


 EXAMPLES = [
	('अग्निः', '', 'प.2.1.19:saṃkhyā-vaṃśyena;input=अग्निः;pos='),
		('रामः', '', 'प.2.1.19:saṃkhyā-vaṃśyena;input=रामः;pos='),
		('सीता', '', 'प.2.1.19:saṃkhyā-vaṃśyena;input=सीता;pos='),
	]
