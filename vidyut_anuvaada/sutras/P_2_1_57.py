# Sutra प.2.1.57: विशेषणं विशेष्येण बहुलम्
# marker: viśeṣaṇaṃ-viśeṣyeṇa-bahulam

from sutra_engines import apply_general

SUTRA_CODE = "प.2.1.57"
SUTRA_TEXT = "विशेषणं विशेष्येण बहुलम्"
SUTRA_DESC = "viśeṣaṇaṃ-viśeṣyeṇa-bahulam"


class Sutra2157:
 def apply(self, word, pos):
  from P_2_1 import apply_2_1_57
  return apply_2_1_57(word, pos)


 EXAMPLES = [
	('अग्निः', '', 'प.2.1.57:viśeṣaṇaṃ-viśeṣyeṇa-bahulam;input=अग्निः;pos='),
		('रामः', '', 'प.2.1.57:viśeṣaṇaṃ-viśeṣyeṇa-bahulam;input=रामः;pos='),
		('सीता', '', 'प.2.1.57:viśeṣaṇaṃ-viśeṣyeṇa-bahulam;input=सीता;pos='),
	]
