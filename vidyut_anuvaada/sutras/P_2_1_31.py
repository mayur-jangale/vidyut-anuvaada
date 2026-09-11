# Sutra प.2.1.31: पूर्वसदृशसमोनार्थकलहनिपुणमिश्रश्लक्ष्णैः
# marker: pūrva-sadṛśa-sama-artha-kalāha-nipuṇa-miśra-ślakṣṇaiḥ

from sutra_engines import apply_general

SUTRA_CODE = "प.2.1.31"
SUTRA_TEXT = "पूर्वसदृशसमोनार्थकलहनिपुणमिश्रश्लक्ष्णैः"
SUTRA_DESC = "pūrva-sadṛśa-sama-artha-kalāha-nipuṇa-miśra-ślakṣṇaiḥ"


class Sutra2131:
 def apply(self, word, pos):
  from P_2_1 import apply_2_1_31
  return apply_2_1_31(word, pos)


 EXAMPLES = [
	('अग्निः', '', 'प.2.1.31:pūrva-sadṛśa-sama-artha-kalāha-nipuṇa-miśra-ślakṣṇaiḥ;input=अग्निः;pos='),
		('रामः', '', 'प.2.1.31:pūrva-sadṛśa-sama-artha-kalāha-nipuṇa-miśra-ślakṣṇaiḥ;input=रामः;pos='),
		('सीता', '', 'प.2.1.31:pūrva-sadṛśa-sama-artha-kalāha-nipuṇa-miśra-ślakṣṇaiḥ;input=सीता;pos='),
	]
