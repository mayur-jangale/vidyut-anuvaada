# Sutra प.2.1.51: तद्धितार्थोत्तरपदसमाहारे च
# marker: taddhitārtha-uttarapada-samāhāre-ca

from sutra_engines import apply_general

SUTRA_CODE = "प.2.1.51"
SUTRA_TEXT = "तद्धितार्थोत्तरपदसमाहारे च"
SUTRA_DESC = "taddhitārtha-uttarapada-samāhāre-ca"


class Sutra2151:
 def apply(self, word, pos):
  from P_2_1 import apply_2_1_51
  return apply_2_1_51(word, pos)


 EXAMPLES = [
	('अग्निः', '', 'प.2.1.51:taddhitārtha-uttarapada-samāhāre-ca;input=अग्निः;pos='),
		('रामः', '', 'प.2.1.51:taddhitārtha-uttarapada-samāhāre-ca;input=रामः;pos='),
		('सीता', '', 'प.2.1.51:taddhitārtha-uttarapada-samāhāre-ca;input=सीता;pos='),
	]
