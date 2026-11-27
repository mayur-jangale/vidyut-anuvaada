"""Clause model: relative and speech clauses (vakya_link), kṛt predicates of verbless half-verses
(vakya_clause), and the particle and determiner rules of vakya. Hand-built readings only."""

from dataclasses import replace

from syntax_fixtures import avyaya, hand, nom, verb

from mayur import compounds, shabdabodha

ACC, NOM, INS = "द्वितीया", "प्रथमा", "तृतीया"


def _resolve(r):
    return shabdabodha.resolve(compounds.annotate(r))


def _lines(r, cut):
    """Put the words from index ``cut`` on in the second half-verse."""
    return replace(r, words=[replace(w, line=0 if k < cut else 1) for k, w in enumerate(r.words)])


def _r(r, form):
    w = next(w for w in r.words if w.form == form)
    return w.role, (r.words[w.head].form if w.head is not None else None)


def _v(form, root, purusha="प्रथमपुरुष", lakara="लट्", prayoga="कर्तरि"):
    return replace(verb(form, root, lakara, prayoga), purusha=purusha)


def test_relative_verb_goes_to_its_correlative():
    r = _resolve(_lines(hand([("यस्", False, [nom("यस्", "यद्", NOM)]),
                              ("पठति", False, [_v("पठति", "पठ्")]),
                              ("सस्", False, [nom("सस्", "तद्", NOM)]),
                              ("जानाति", False, [_v("जानाति", "ज्ञा")])]), 2))
    assert _r(r, "पठति") == ("क्रिया", "सस्")  # 8.1.66, यत्तदोर्नित्यसम्बन्धः
    assert _r(r, "सस्") == ("कर्ता", "जानाति") and _r(r, "जानाति") == ("क्रिया", None)


def test_relative_adverb_goes_to_the_main_verb():
    r = _resolve(_lines(hand([("यदा", False, [avyaya("यदा")]),
                              ("रामस्", False, [nom("रामस्", "राम", NOM)]),
                              ("गच्छति", False, [_v("गच्छति", "गम्")]),
                              ("तदा", False, [avyaya("तदा")]),
                              ("सीता", False, [nom("सीता", "सीता", NOM, "स्त्रीलिङ्ग")]),
                              ("रोदिति", False, [_v("रोदिति", "रुद्")])]), 3))
    assert _r(r, "गच्छति") == ("क्रिया", "रोदिति")


def test_coordinated_relative_is_no_clause_marker():
    r = _resolve(_lines(hand([("ददौ", False, [verb("ददौ", "दा")]),
                              ("यत्", False, [nom("यत्", "यद्", ACC, "नपुंसकलिङ्ग")]),
                              ("च", False, [avyaya("च")]),
                              ("तत्", False, [nom("तत्", "तद्", ACC, "नपुंसकलिङ्ग")]),
                              ("आनयत्", False, [verb("आनयत्", "नी", "लङ्")])]), 3))
    assert _r(r, "ददौ")[1] is None  # यत् च: an elliptic co-ordinate, not a relative clause


def test_speech_after_a_frame():
    r = _resolve(_lines(hand([("शिवस्", False, [nom("शिवस्", "शिव", NOM)]),
                              ("उवाच", False, [verb("उवाच", "वच्")]),
                              ("अहम्", False, [nom("अहम्", "अस्मद्", NOM, None)]),
                              ("गच्छामि", False, [_v("गच्छामि", "गम्", "उत्तमपुरुष")])]), 2))
    assert _r(r, "गच्छामि") == ("क्रिया", "उवाच")  # the words spoken: कर्म of the verb of saying (1.4.49)


def test_third_person_after_speech_verb_stays_main():
    r = _resolve(_lines(hand([("रामस्", False, [nom("रामस्", "राम", NOM)]),
                              ("वाक्यम्", False, [nom("वाक्यम्", "वाक्य", ACC, "नपुंसकलिङ्ग")]),
                              ("उवाच", False, [verb("उवाच", "वच्")]),
                              ("सीता", False, [nom("सीता", "सीता", NOM, "स्त्रीलिङ्ग")]),
                              ("जगाम", False, [verb("जगाम", "गम्")])]), 3))
    assert _r(r, "जगाम") == ("क्रिया", None)


def test_kta_predicate_of_a_prose_sentence_governs_absolutive_and_agent():
    r = _resolve(hand([("अथ", False, [avyaya("अथ")]),
                       ("सारसेन", False, [nom("सारसेन", "सारस", INS)]),
                       ("उपसृत्य", False, [avyaya("उपसृत्य", krt="ल्यप्")]),
                       ("राजा", False, [nom("राजा", "राजन्", NOM)]),
                       ("क्षिप्तस्", False, [replace(nom("क्षिप्तस्", "क्षिप्", NOM, krt="क्त"), root="क्षिप्")])]))
    assert _r(r, "सारसेन") == ("कर्ता", "क्षिप्तस्")  # 2.3.18: the agent the क्त does not express
    assert _r(r, "उपसृत्य")[1] == "क्षिप्तस्"
    assert _r(r, "अथ")[1] == "क्षिप्तस्"  # the connective goes to the main action, not the absolutive


def test_instrumental_beside_a_kartari_kta_is_no_agent():
    r = _resolve(hand([("सुग्रीवेण", False, [nom("सुग्रीवेण", "सुग्रीव", INS)]),
                       ("समागतस्", False, [replace(nom("समागतस्", "समागत", NOM, krt="क्त"), root="गम्")]),
                       ("रामस्", False, [nom("रामस्", "राम", NOM)])]))
    assert _r(r, "सुग्रीवेण")[0] == "करण"  # 3.4.72: the क्त of गम् is कर्तरि, so 2.3.1 bars an agent तृतीया


def test_pronoun_delimits_in_a_negated_verbless_half_verse():
    r = _resolve(_lines(hand([("जन्तवस्", False, [nom("जन्तवस्", "जन्तु", NOM, vacana="बहुवचन")]),
                              ("मज्जन्ति", False, [replace(_v("मज्जन्ति", "मज्ज्"), vacana="बहुवचन")]),
                              ("न", False, [avyaya("न")]),
                              ("भयम्", False, [nom("भयम्", "भय", NOM, "नपुंसकलिङ्ग")]),
                              ("किंचिद्", False, [nom("किंचिद्", "कश्चित्", NOM, "नपुंसकलिङ्ग")])]), 2))
    assert _r(r, "भयम्") == ("कर्ता", None)  # its own clause: न denies existence, अस्ति supplied
    assert _r(r, "न")[1] == "भयम्"
    assert _r(r, "किंचिद्") == ("विशेषण", "भयम्")


GEN = "षष्ठी"


def test_enclitic_genitive_leans_on_the_noun_before_it():
    r = _resolve(hand([("अधिकारस्", False, [nom("अधिकारस्", "अधिकार", NOM)]),
                       ("ते", False, [nom("ते", "युष्मद्", GEN, None)]),
                       ("फलेषु", False, [nom("फलेषु", "फल", "सप्तमी", "नपुंसकलिङ्ग", "बहुवचन")])]))
    assert _r(r, "ते") == ("सम्बन्ध", "अधिकारस्")  # 8.1.18, 8.1.22: ते never opens a pāda


def test_personal_genitive_owns_the_next_genitive_noun():
    r = _resolve(hand([("मम", False, [nom("मम", "अस्मद्", GEN)]),
                       ("मित्रस्य", False, [nom("मित्रस्य", "मित्र", GEN)]),
                       ("पुत्रस्", False, [nom("पुत्रस्", "पुत्र", NOM)]),
                       ("अस्ति", False, [verb("अस्ति", "अस्", "लट्")])]))
    assert _r(r, "मम") == ("सम्बन्ध", "मित्रस्य")
    assert _r(r, "मित्रस्य") == ("सम्बन्ध", "पुत्रस्")


def test_numeral_counts_its_noun():
    r = _resolve(hand([("पञ्च", False, [nom("पञ्च", "पञ्चन्", NOM, vacana="बहुवचन")]),
                       ("बालकास्", False, [nom("बालकास्", "बालक", NOM, vacana="बहुवचन")]),
                       ("क्रीडन्ति", False, [replace(_v("क्रीडन्ति", "क्रीड्"), vacana="बहुवचन")])]))
    assert _r(r, "बालकास्") == ("कर्ता", "क्रीडन्ति") and _r(r, "पञ्च") == ("विशेषण", "बालकास्")
