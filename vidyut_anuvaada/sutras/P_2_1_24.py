# Sutra प.2.1.24: द्वितीया श्रितातीतपतितगतात्यस्तप्राप्तापन्नैः
# marker: dvitīyā-śritātīta-patita-gatātyasta-prāptāpannaiḥ

from sutra_engines import apply_general

SUTRA_CODE = "प.2.1.24"
SUTRA_TEXT = "द्वितीया श्रितातीतपतितगतात्यस्तप्राप्तापन्नैः"
SUTRA_DESC = "dvitīyā-śritātīta-patita-gatātyasta-prāptāpannaiḥ"


class Sutra2124:
 def apply(self, word, pos):
  from P_2_1 import apply_2_1_24
  return apply_2_1_24(word, pos)


 EXAMPLES = [
	('अग्निः', '', 'प.2.1.24:dvitīyā-śritātīta-patita-gatātyasta-prāptāpannaiḥ;input=अग्निः;pos='),
		('रामः', '', 'प.2.1.24:dvitīyā-śritātīta-patita-gatātyasta-prāptāpannaiḥ;input=रामः;pos='),
		('सीता', '', 'प.2.1.24:dvitīyā-śritātīta-patita-gatātyasta-prāptāpannaiḥ;input=सीता;pos='),
	]
