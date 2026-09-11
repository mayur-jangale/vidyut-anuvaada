# Sutra प.2.1.42: ध्वाङ्क्षेण क्षेपे
# marker: dhvāṅkṣeṇa-kṣepe

from sutra_engines import apply_general

SUTRA_CODE = "प.2.1.42"
SUTRA_TEXT = "ध्वाङ्क्षेण क्षेपे"
SUTRA_DESC = "dhvāṅkṣeṇa-kṣepe"


class Sutra2142:
 def apply(self, word, pos):
  from P_2_1 import apply_2_1_42
  return apply_2_1_42(word, pos)


 EXAMPLES = [
	('अग्निः', '', 'प.2.1.42:dhvāṅkṣeṇa-kṣepe;input=अग्निः;pos='),
		('रामः', '', 'प.2.1.42:dhvāṅkṣeṇa-kṣepe;input=रामः;pos='),
		('सीता', '', 'प.2.1.42:dhvāṅkṣeṇa-kṣepe;input=सीता;pos='),
	]
