# Sutra प.2.1.16: यस्य चायामः
# marker: yasya-cāyāma

from sutra_engines import apply_general

SUTRA_CODE = "प.2.1.16"
SUTRA_TEXT = "यस्य चायामः"
SUTRA_DESC = "yasya-cāyāma"


class Sutra2116:
 def apply(self, word, pos):
  from P_2_1 import apply_2_1_16
  return apply_2_1_16(word, pos)


 EXAMPLES = [
	('अग्निः', '', 'प.2.1.16:yasya-cāyāma;input=अग्निः;pos='),
		('रामः', '', 'प.2.1.16:yasya-cāyāma;input=रामः;pos='),
		('सीता', '', 'प.2.1.16:yasya-cāyāma;input=सीता;pos='),
	]
