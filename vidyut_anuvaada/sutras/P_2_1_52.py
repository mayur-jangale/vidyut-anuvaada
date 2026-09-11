# Sutra प.2.1.52: संख्या पूर्वो द्विगुः
# marker: saṃkhyā-pūrvo-dviguḥ

from sutra_engines import apply_general

SUTRA_CODE = "प.2.1.52"
SUTRA_TEXT = "संख्या पूर्वो द्विगुः"
SUTRA_DESC = "saṃkhyā-pūrvo-dviguḥ"


class Sutra2152:
 def apply(self, word, pos):
  from P_2_1 import apply_2_1_52
  return apply_2_1_52(word, pos)


 EXAMPLES = [
	('अग्निः', '', 'प.2.1.52:saṃkhyā-pūrvo-dviguḥ;input=अग्निः;pos='),
		('रामः', '', 'प.2.1.52:saṃkhyā-pūrvo-dviguḥ;input=रामः;pos='),
		('सीता', '', 'प.2.1.52:saṃkhyā-pūrvo-dviguḥ;input=सीता;pos='),
	]
