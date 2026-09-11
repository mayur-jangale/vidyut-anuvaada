# Sutra प.2.1.32: कर्तृकरणे कृता बहुलम्
# marker: kartṛ-karaṇe-kṛtā-bahulam

from sutra_engines import apply_general

SUTRA_CODE = "प.2.1.32"
SUTRA_TEXT = "कर्तृकरणे कृता बहुलम्"
SUTRA_DESC = "kartṛ-karaṇe-kṛtā-bahulam"


class Sutra2132:
 def apply(self, word, pos):
  from P_2_1 import apply_2_1_32
  return apply_2_1_32(word, pos)


 EXAMPLES = [
	('अग्निः', '', 'प.2.1.32:kartṛ-karaṇe-kṛtā-bahulam;input=अग्निः;pos='),
		('रामः', '', 'प.2.1.32:kartṛ-karaṇe-kṛtā-bahulam;input=रामः;pos='),
		('सीता', '', 'प.2.1.32:kartṛ-karaṇe-kṛtā-bahulam;input=सीता;pos='),
	]
