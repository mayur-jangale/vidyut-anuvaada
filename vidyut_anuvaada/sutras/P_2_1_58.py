# Sutra प.2.1.58: पूर्वापरप्रथमचरमजघन्यसमानमध्यमध्यमवीराश्च
# marker: pūrvāpara-prathama-carama-jaghanya-samāna-madhya-madhya-vīrāśca

from sutra_engines import apply_general

SUTRA_CODE = "प.2.1.58"
SUTRA_TEXT = "पूर्वापरप्रथमचरमजघन्यसमानमध्यमध्यमवीराश्च"
SUTRA_DESC = "pūrvāpara-prathama-carama-jaghanya-samāna-madhya-madhya-vīrāśca"


class Sutra2158:
 def apply(self, word, pos):
  from P_2_1 import apply_2_1_58
  return apply_2_1_58(word, pos)


 EXAMPLES = [
	('अग्निः', '', 'प.2.1.58:pūrvāpara-prathama-carama-jaghanya-samāna-madhya-madhya-vīrāśca;input=अग्निः;pos='),
		('रामः', '', 'प.2.1.58:pūrvāpara-prathama-carama-jaghanya-samāna-madhya-madhya-vīrāśca;input=रामः;pos='),
		('सीता', '', 'प.2.1.58:pūrvāpara-prathama-carama-jaghanya-samāna-madhya-madhya-vīrāśca;input=सीता;pos='),
	]
