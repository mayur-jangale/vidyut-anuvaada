# Sutra प.2.1.65: पोटायुवतिस्तोककतिपयगृष्टिधेनुवशावेहत्बष्कयणीप्रवक्तृश्रोत्रियाध्यापकधूर्तैर्जातिः
# marker: poṭā-yuvati

from sutra_engines import apply_general

SUTRA_CODE = "प.2.1.65"
SUTRA_TEXT = "पोटायुवतिस्तोककतिपयगृष्टिधेनुवशावेहत्बष्कयणीप्रवक्तृश्रोत्रियाध्यापकधूर्तैर्जातिः"
SUTRA_DESC = "poṭā-yuvati"


class Sutra2165:
 def apply(self, word, pos):
  from P_2_1 import apply_2_1_65
  return apply_2_1_65(word, pos)


 EXAMPLES = [
	('अग्निः', '', 'प.2.1.65:poṭā-yuvati;input=अग्निः;pos='),
		('रामः', '', 'प.2.1.65:poṭā-yuvati;input=रामः;pos='),
		('सीता', '', 'प.2.1.65:poṭā-yuvati;input=सीता;pos='),
	]
