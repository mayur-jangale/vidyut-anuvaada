# Sutra प.1.3.32: गन्धनावक्षेपणसेवनसाहसिक्यप्रतियत्नप्रकथनोपयोगेषु कृञः
from P_1_3 import apply_1_3_32


class Sutra1332:
	def apply(self, word, pos):
		return apply_1_3_32(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'kandhanAvakzepaRasevanasAhasikyapratiyatnaprakaTanopayogeRu:अग्निः;n/a'),
		('रामः', '', 'kandhanAvakzepaRasevanasAhasikyapratiyatnaprakaTanopayogeRu:रामः;n/a'),
		('सीता', '', 'kandhanAvakzepaRasevanasAhasikyapratiyatnaprakaTanopayogeRu:सीता;n/a'),
	]

