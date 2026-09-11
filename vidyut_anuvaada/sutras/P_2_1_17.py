# Sutra प.2.1.17: तिष्ठद्गुप्रभृतीनि च
# marker: tiṣṭhadgu-prabhṛtīni-ca

from sutra_engines import apply_general

SUTRA_CODE = "प.2.1.17"
SUTRA_TEXT = "तिष्ठद्गुप्रभृतीनि च"
SUTRA_DESC = "tiṣṭhadgu-prabhṛtīni-ca"


class Sutra2117:
 def apply(self, word, pos):
  from P_2_1 import apply_2_1_17
  return apply_2_1_17(word, pos)


 EXAMPLES = [
	('अग्निः', '', 'प.2.1.17:tiṣṭhadgu-prabhṛtīni-ca;input=अग्निः;pos='),
		('रामः', '', 'प.2.1.17:tiṣṭhadgu-prabhṛtīni-ca;input=रामः;pos='),
		('सीता', '', 'प.2.1.17:tiṣṭhadgu-prabhṛtīni-ca;input=सीता;pos='),
	]
