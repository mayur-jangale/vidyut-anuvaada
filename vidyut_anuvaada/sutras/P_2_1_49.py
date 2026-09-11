# Sutra प.2.1.49: पूर्वकालैकसर्वजरत्पुराणनवकेवलाः समानाधिकरणेन
# marker: pūrvakāla-eka-sarva-jaral-purāṇa-nava-kevalaḥ

from sutra_engines import apply_general

SUTRA_CODE = "प.2.1.49"
SUTRA_TEXT = "पूर्वकालैकसर्वजरत्पुराणनवकेवलाः समानाधिकरणेन"
SUTRA_DESC = "pūrvakāla-eka-sarva-jaral-purāṇa-nava-kevalaḥ"


class Sutra2149:
 def apply(self, word, pos):
  from P_2_1 import apply_2_1_49
  return apply_2_1_49(word, pos)


 EXAMPLES = [
	('अग्निः', '', 'प.2.1.49:pūrvakāla-eka-sarva-jaral-purāṇa-nava-kevalaḥ;input=अग्निः;pos='),
		('रामः', '', 'प.2.1.49:pūrvakāla-eka-sarva-jaral-purāṇa-nava-kevalaḥ;input=रामः;pos='),
		('सीता', '', 'प.2.1.49:pūrvakāla-eka-sarva-jaral-purāṇa-nava-kevalaḥ;input=सीता;pos='),
	]
