# Sutra प10: prayE rohizyE avyaTizyE
# prayE rohiSye avyaTiSye

from sutra_engines import apply_general
from P_3_4 import apply_3_4_10

SUTRA_CODE = "प10"
SUTRA_TEXT = "prayE rohizyE avyaTizyE"
SUTRA_DESC = "prayE rohiSye avyaTiSye"


class Sutra3410:
	def apply(self, word, pos):
		return apply_3_4_10(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'p34-010:prayE rohiSye avyaTiSye;input=अग्निः;stem=अग्निः;ending=-;pos='),
		('रामः', '', 'p34-010:prayE rohiSye avyaTiSye;input=रामः;stem=रामः;ending=-;pos='),
		('सीता', '', 'p34-010:prayE rohiSye avyaTiSye;input=सीता;stem=सीता;ending=-;pos='),
	]

