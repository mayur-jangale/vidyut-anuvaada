# Sutra प.2.1.61: सन्महत्परमोत्तमोत्कृष्टाः पूज्यमानैः
# marker: san-mahat-parama-uttama-utkṛṣṭāḥ

from sutra_engines import apply_general

SUTRA_CODE = "प.2.1.61"
SUTRA_TEXT = "सन्महत्परमोत्तमोत्कृष्टाः पूज्यमानैः"
SUTRA_DESC = "san-mahat-parama-uttama-utkṛṣṭāḥ"


class Sutra2161:
 def apply(self, word, pos):
  from P_2_1 import apply_2_1_61
  return apply_2_1_61(word, pos)


 EXAMPLES = [
	('अग्निः', '', 'प.2.1.61:san-mahat-parama-uttama-utkṛṣṭāḥ;input=अग्निः;pos='),
		('रामः', '', 'प.2.1.61:san-mahat-parama-uttama-utkṛṣṭāḥ;input=रामः;pos='),
		('सीता', '', 'प.2.1.61:san-mahat-parama-uttama-utkṛṣṭāḥ;input=सीता;pos='),
	]
