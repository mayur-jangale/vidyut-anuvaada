# Sutra प.2.1.38: अपेतापोढमुक्तपतितापत्रस्तैरल्पशः
# marker: apeta-āpoḍha-mukta-patitāpatra-stair-alpaśaḥ

from sutra_engines import apply_general

SUTRA_CODE = "प.2.1.38"
SUTRA_TEXT = "अपेतापोढमुक्तपतितापत्रस्तैरल्पशः"
SUTRA_DESC = "apeta-āpoḍha-mukta-patitāpatra-stair-alpaśaḥ"


class Sutra2138:
 def apply(self, word, pos):
  from P_2_1 import apply_2_1_38
  return apply_2_1_38(word, pos)


 EXAMPLES = [
	('अग्निः', '', 'प.2.1.38:apeta-āpoḍha-mukta-patitāpatra-stair-alpaśaḥ;input=अग्निः;pos='),
		('रामः', '', 'प.2.1.38:apeta-āpoḍha-mukta-patitāpatra-stair-alpaśaḥ;input=रामः;pos='),
		('सीता', '', 'प.2.1.38:apeta-āpoḍha-mukta-patitāpatra-stair-alpaśaḥ;input=सीता;pos='),
	]
