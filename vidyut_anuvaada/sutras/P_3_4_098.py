# Sutra प98: sa uttamasya
# sa uttamasya

from sutra_engines import apply_general
from P_3_4 import apply_3_4_98

SUTRA_CODE = "प98"
SUTRA_TEXT = "sa uttamasya"
SUTRA_DESC = "sa uttamasya"


class Sutra3498:
	def apply(self, word, pos):
		return apply_3_4_98(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'p34-098:sa uttamasya;input=अग्निः;stem=अग्निः;ending=-;pos='),
		('रामः', '', 'p34-098:sa uttamasya;input=रामः;stem=रामः;ending=-;pos='),
		('सीता', '', 'p34-098:sa uttamasya;input=सीता;stem=सीता;ending=-;pos='),
	]

