# Sutra प.2.1.35: भक्ष्येण मिश्रीकरणम्
# marker: bhakṣya-miśrīkaraṇam

from sutra_engines import apply_general

SUTRA_CODE = "प.2.1.35"
SUTRA_TEXT = "भक्ष्येण मिश्रीकरणम्"
SUTRA_DESC = "bhakṣya-miśrīkaraṇam"


class Sutra2135:
 def apply(self, word, pos):
  from P_2_1 import apply_2_1_35
  return apply_2_1_35(word, pos)


 EXAMPLES = [
	('अग्निः', '', 'प.2.1.35:bhakṣya-miśrīkaraṇam;input=अग्निः;pos='),
		('रामः', '', 'प.2.1.35:bhakṣya-miśrīkaraṇam;input=रामः;pos='),
		('सीता', '', 'प.2.1.35:bhakṣya-miśrīkaraṇam;input=सीता;pos='),
	]
