# Sutra प59: avyaye kfYaH ktvA Ramul
# avyaye'yaTABipretAKyAne kfYaH

from sutra_engines import apply_general
from P_3_4 import apply_3_4_59

SUTRA_CODE = "प59"
SUTRA_TEXT = "avyaye kfYaH ktvA Ramul"
SUTRA_DESC = "avyaye'yaTABipretAKyAne kfYaH"


class Sutra3459:
	def apply(self, word, pos):
		return apply_3_4_59(word, pos)

	EXAMPLES = [
	('अग्निः', '', "p34-059:avyaye'yaTABipretAKyAne kfYaH;input=अग्निः;stem=अग्निः;ending=-;pos="),
		('रामः', '', "p34-059:avyaye'yaTABipretAKyAne kfYaH;input=रामः;stem=रामः;ending=-;pos="),
		('सीता', '', "p34-059:avyaye'yaTABipretAKyAne kfYaH;input=सीता;stem=सीता;ending=-;pos="),
	]

