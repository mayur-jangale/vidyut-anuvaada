# Sutra प.2.1.36: चतुर्थी तदर्थार्थबलिहितसुखरक्षितैः
# marker: caturthī-tadarthārtha-bali-hita-sukha-rakṣitaiḥ

from sutra_engines import apply_general

SUTRA_CODE = "प.2.1.36"
SUTRA_TEXT = "चतुर्थी तदर्थार्थबलिहितसुखरक्षितैः"
SUTRA_DESC = "caturthī-tadarthārtha-bali-hita-sukha-rakṣitaiḥ"


class Sutra2136:
 def apply(self, word, pos):
  from P_2_1 import apply_2_1_36
  return apply_2_1_36(word, pos)


 EXAMPLES = [
	('अग्निः', '', 'प.2.1.36:caturthī-tadarthārtha-bali-hita-sukha-rakṣitaiḥ;input=अग्निः;pos='),
		('रामः', '', 'प.2.1.36:caturthī-tadarthārtha-bali-hita-sukha-rakṣitaiḥ;input=रामः;pos='),
		('सीता', '', 'प.2.1.36:caturthī-tadarthārtha-bali-hita-sukha-rakṣitaiḥ;input=सीता;pos='),
	]
