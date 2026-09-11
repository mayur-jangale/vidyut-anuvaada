# Sutra प.2.1.67: युवा खलतिपलितवलिनजरतीभिः
# marker: yuvā-khalati-palita-valina-jaratībhyaḥ

from sutra_engines import apply_general

SUTRA_CODE = "प.2.1.67"
SUTRA_TEXT = "युवा खलतिपलितवलिनजरतीभिः"
SUTRA_DESC = "yuvā-khalati-palita-valina-jaratībhyaḥ"


class Sutra2167:
 def apply(self, word, pos):
  from P_2_1 import apply_2_1_67
  return apply_2_1_67(word, pos)


 EXAMPLES = [
	('अग्निः', '', 'प.2.1.67:yuvā-khalati-palita-valina-jaratībhyaḥ;input=अग्निः;pos='),
		('रामः', '', 'प.2.1.67:yuvā-khalati-palita-valina-jaratībhyaḥ;input=रामः;pos='),
		('सीता', '', 'प.2.1.67:yuvā-khalati-palita-valina-jaratībhyaḥ;input=सीता;pos='),
	]
