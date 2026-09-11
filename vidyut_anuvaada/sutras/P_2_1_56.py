# Sutra प.2.1.56: उपमितं व्याघ्रादिभिः सामान्याप्रयोगे
# marker: upamitaṃ-vyāghrādibhiḥ

from sutra_engines import apply_general

SUTRA_CODE = "प.2.1.56"
SUTRA_TEXT = "उपमितं व्याघ्रादिभिः सामान्याप्रयोगे"
SUTRA_DESC = "upamitaṃ-vyāghrādibhiḥ"


class Sutra2156:
 def apply(self, word, pos):
  from P_2_1 import apply_2_1_56
  return apply_2_1_56(word, pos)


 EXAMPLES = [
	('अग्निः', '', 'प.2.1.56:upamitaṃ-vyāghrādibhiḥ;input=अग्निः;pos='),
		('रामः', '', 'प.2.1.56:upamitaṃ-vyāghrādibhiḥ;input=रामः;pos='),
		('सीता', '', 'प.2.1.56:upamitaṃ-vyāghrādibhiḥ;input=सीता;pos='),
	]
