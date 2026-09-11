# Sutra प.2.1.29: अत्यन्तसंयोगे च
# marker: atyanta-saṃyoge-ca

from sutra_engines import apply_general

SUTRA_CODE = "प.2.1.29"
SUTRA_TEXT = "अत्यन्तसंयोगे च"
SUTRA_DESC = "atyanta-saṃyoge-ca"


class Sutra2129:
 def apply(self, word, pos):
  from P_2_1 import apply_2_1_29
  return apply_2_1_29(word, pos)


 EXAMPLES = [
	('अग्निः', '', 'प.2.1.29:atyanta-saṃyoge-ca;input=अग्निः;pos='),
		('रामः', '', 'प.2.1.29:atyanta-saṃyoge-ca;input=रामः;pos='),
		('सीता', '', 'प.2.1.29:atyanta-saṃyoge-ca;input=सीता;pos='),
	]
