# Sutra प.2.1.6: अव्ययं विभक्तिसमीपसमृद्धिव्यृद्ध्यर्थाभावात्ययासम्प्रतिशब्दप्रादुर्भावपश्चाद्यथानुपूर्व्ययौगपद्यसादृश्यसम्पत्तिसाकल्यान्तवचनेषु
# marker: avyayībhāva-formed

from sutra_engines import apply_general

SUTRA_CODE = "प.2.1.6"
SUTRA_TEXT = "अव्ययं विभक्तिसमीपसमृद्धिव्यृद्ध्यर्थाभावात्ययासम्प्रतिशब्दप्रादुर्भावपश्चाद्यथानुपूर्व्ययौगपद्यसादृश्यसम्पत्तिसाकल्यान्तवचनेषु"
SUTRA_DESC = "avyayībhāva-formed"


class Sutra216:
 def apply(self, word, pos):
  from P_2_1 import apply_2_1_6
  return apply_2_1_6(word, pos)


 EXAMPLES = [
	('अग्निः', '', 'प.2.1.6:avyayībhāva-formed;input=अग्निः;pos='),
		('रामः', '', 'प.2.1.6:avyayībhāva-formed;input=रामः;pos='),
		('सीता', '', 'प.2.1.6:avyayībhāva-formed;input=सीता;pos='),
	]
