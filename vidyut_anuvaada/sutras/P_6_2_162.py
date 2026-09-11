# Sutra प.6.2.162: बहुव्रीहाविदमेतत्तद्भ्यः प्रथमपूरणयोः क्रियागणने
# (Sandhi (euphonic combination)) — bahuvrIhAvidametattadByaH praTamapUraRayoH kriyAgaRane

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.162"
SUTRA_TEXT = "बहुव्रीहाविदमेतत्तद्भ्यः प्रथमपूरणयोः क्रियागणने"
SUTRA_DESC = "(Sandhi (euphonic combination)) — bahuvrIhAvidametattadByaH praTamapUraRayoH kriyAgaRane"


class Sutra62162:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.162: अग्निः'),
		('रामः', '', 'प.6.2.162: रामः'),
		('सीता', '', 'प.6.2.162: सीता'),
	]

