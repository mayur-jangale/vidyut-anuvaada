# Sutra प.2.1.62: वृन्दारकनागकुञ्जरैः पूज्यमानम्
# marker: vṛndāraka-nāga-kuñjaraiḥ

from sutra_engines import apply_general

SUTRA_CODE = "प.2.1.62"
SUTRA_TEXT = "वृन्दारकनागकुञ्जरैः पूज्यमानम्"
SUTRA_DESC = "vṛndāraka-nāga-kuñjaraiḥ"


class Sutra2162:
 def apply(self, word, pos):
  from P_2_1 import apply_2_1_62
  return apply_2_1_62(word, pos)


 EXAMPLES = [
	('अग्निः', '', 'प.2.1.62:vṛndāraka-nāga-kuñjaraiḥ;input=अग्निः;pos='),
		('रामः', '', 'प.2.1.62:vṛndāraka-nāga-kuñjaraiḥ;input=रामः;pos='),
		('सीता', '', 'प.2.1.62:vṛndāraka-nāga-kuñjaraiḥ;input=सीता;pos='),
	]
