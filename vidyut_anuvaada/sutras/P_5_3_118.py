# Sutra प.5.3.118: अभिजिद्विदभृच्छालावच्छिखावच्छमीवदूर्णावच्छ्रुमदणो यञ्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — aBijidvidaBfcCAlAvacCiKAvacCamIvadUrRAvacCrumadaRo yaY

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.118"
SUTRA_TEXT = "अभिजिद्विदभृच्छालावच्छिखावच्छमीवदूर्णावच्छ्रुमदणो यञ्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — aBijidvidaBfcCAlAvacCiKAvacCamIvadUrRAvacCrumadaRo yaY"


class Sutra53118:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.118: अग्निः'),
		('रामः', '', 'प.5.3.118: रामः'),
		('सीता', '', 'प.5.3.118: सीता'),
	]

