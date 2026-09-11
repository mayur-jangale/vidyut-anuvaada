# Sutra प.7.2.34: ग्रसितस्कभितस्तभितोत्तभितचत्तविकस्ताविशस्तृशंस्तृशास्तृतरुतृतरूतृवरुतृवरूतृवरूत्रीरुज्ज्वलितिक्षरितिक्षमितिवमित्यमितीति च
# (Taddhita (secondary derivations)) — grasitaskaBitastaBitottaBitacattavikastAviSastfSaMstfSAstftarutftarUtfvarutfvarUtfvarUtrIrujjvalitikzaritikzamitivamityamitIti ca

from sutra_engines import apply_general

SUTRA_CODE = "प.7.2.34"
SUTRA_TEXT = "ग्रसितस्कभितस्तभितोत्तभितचत्तविकस्ताविशस्तृशंस्तृशास्तृतरुतृतरूतृवरुतृवरूतृवरूत्रीरुज्ज्वलितिक्षरितिक्षमितिवमित्यमितीति च"
SUTRA_DESC = "(Taddhita (secondary derivations)) — grasitaskaBitastaBitottaBitacattavikastAviSastfSaMstfSAstftarutftarUtfvarutfvarUtfvarUtrIrujjvalitikzaritikzamitivamityamitIti ca"


class Sutra7234:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.2.34: अग्निः'),
		('रामः', '', 'प.7.2.34: रामः'),
		('सीता', '', 'प.7.2.34: सीता'),
	]

