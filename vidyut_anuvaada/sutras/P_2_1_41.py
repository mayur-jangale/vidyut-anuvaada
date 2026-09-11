# Sutra प.2.1.41: सिद्धशुष्कपक्वबन्धैश्च
# marker: siddha-śuṣka-pakva-bandhaiś-ca

from sutra_engines import apply_general

SUTRA_CODE = "प.2.1.41"
SUTRA_TEXT = "सिद्धशुष्कपक्वबन्धैश्च"
SUTRA_DESC = "siddha-śuṣka-pakva-bandhaiś-ca"


class Sutra2141:
 def apply(self, word, pos):
  from P_2_1 import apply_2_1_41
  return apply_2_1_41(word, pos)


 EXAMPLES = [
	('अग्निः', '', 'प.2.1.41:siddha-śuṣka-pakva-bandhaiś-ca;input=अग्निः;pos='),
		('रामः', '', 'प.2.1.41:siddha-śuṣka-pakva-bandhaiś-ca;input=रामः;pos='),
		('सीता', '', 'प.2.1.41:siddha-śuṣka-pakva-bandhaiś-ca;input=सीता;pos='),
	]
