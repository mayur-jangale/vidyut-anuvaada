# Sutra प.2.1.5: अव्ययीभावः
# marker: avyayībhāva-declared

from sutra_engines import apply_general

SUTRA_CODE = "प.2.1.5"
SUTRA_TEXT = "अव्ययीभावः"
SUTRA_DESC = "avyayībhāva-declared"


class Sutra215:
 def apply(self, word, pos):
  from P_2_1 import apply_2_1_5
  return apply_2_1_5(word, pos)


 EXAMPLES = [
	('अग्निः', '', 'प.2.1.5:avyayībhāva-declared;input=अग्निः;pos='),
		('रामः', '', 'प.2.1.5:avyayībhāva-declared;input=रामः;pos='),
		('सीता', '', 'प.2.1.5:avyayībhāva-declared;input=सीता;pos='),
	]
