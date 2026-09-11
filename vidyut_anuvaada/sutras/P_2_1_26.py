# Sutra प.2.1.26: खट्वा क्षेपे
# marker: khaṭvā-kṣepe

from sutra_engines import apply_general

SUTRA_CODE = "प.2.1.26"
SUTRA_TEXT = "खट्वा क्षेपे"
SUTRA_DESC = "khaṭvā-kṣepe"


class Sutra2126:
 def apply(self, word, pos):
  from P_2_1 import apply_2_1_26
  return apply_2_1_26(word, pos)


 EXAMPLES = [
	('अग्निः', '', 'प.2.1.26:khaṭvā-kṣepe;input=अग्निः;pos='),
		('रामः', '', 'प.2.1.26:khaṭvā-kṣepe;input=रामः;pos='),
		('सीता', '', 'प.2.1.26:khaṭvā-kṣepe;input=सीता;pos='),
	]
