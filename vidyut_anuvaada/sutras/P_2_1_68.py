# Sutra प.2.1.68: कृत्यतुल्याख्या अजात्या
# marker: kṛtya-tulyākhyā-ajātyā

from sutra_engines import apply_general

SUTRA_CODE = "प.2.1.68"
SUTRA_TEXT = "कृत्यतुल्याख्या अजात्या"
SUTRA_DESC = "kṛtya-tulyākhyā-ajātyā"


class Sutra2168:
 def apply(self, word, pos):
  from P_2_1 import apply_2_1_68
  return apply_2_1_68(word, pos)


 EXAMPLES = [
	('अग्निः', '', 'प.2.1.68:kṛtya-tulyākhyā-ajātyā;input=अग्निः;pos='),
		('रामः', '', 'प.2.1.68:kṛtya-tulyākhyā-ajātyā;input=रामः;pos='),
		('सीता', '', 'प.2.1.68:kṛtya-tulyākhyā-ajātyā;input=सीता;pos='),
	]
