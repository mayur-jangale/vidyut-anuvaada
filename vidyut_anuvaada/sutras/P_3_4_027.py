# Sutra प27: anyaTA siddha prayogaH cet
# anyaTA evaM kaTam itTaMsu

from sutra_engines import apply_general
from P_3_4 import apply_3_4_27

SUTRA_CODE = "प27"
SUTRA_TEXT = "anyaTA siddha prayogaH cet"
SUTRA_DESC = "anyaTA evaM kaTam itTaMsu"


class Sutra3427:
	def apply(self, word, pos):
		return apply_3_4_27(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'p34-027:anyaTA evaM kaTam itTaMsu;input=अग्निः;stem=अग्निः;ending=-;pos='),
		('रामः', '', 'p34-027:anyaTA evaM kaTam itTaMsu;input=रामः;stem=रामः;ending=-;pos='),
		('सीता', '', 'p34-027:anyaTA evaM kaTam itTaMsu;input=सीता;stem=सीता;ending=-;pos='),
	]

