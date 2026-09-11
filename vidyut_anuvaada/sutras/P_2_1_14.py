# Sutra प.2.1.14: लक्षणेनाभिप्रती आभिमुख्ये
# marker: lakṣaṇenābhipratī-ābhīmukhya

from sutra_engines import apply_general

SUTRA_CODE = "प.2.1.14"
SUTRA_TEXT = "लक्षणेनाभिप्रती आभिमुख्ये"
SUTRA_DESC = "lakṣaṇenābhipratī-ābhīmukhya"


class Sutra2114:
 def apply(self, word, pos):
  from P_2_1 import apply_2_1_14
  return apply_2_1_14(word, pos)


 EXAMPLES = [
	('अग्निः', '', 'प.2.1.14:lakṣaṇenābhipratī-ābhīmukhya;input=अग्निः;pos='),
		('रामः', '', 'प.2.1.14:lakṣaṇenābhipratī-ābhīmukhya;input=रामः;pos='),
		('सीता', '', 'प.2.1.14:lakṣaṇenābhipratī-ābhīmukhya;input=सीता;pos='),
	]
