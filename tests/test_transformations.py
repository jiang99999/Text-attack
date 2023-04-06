def test_imports():
    import flair
    import torch

    import textattack

    del textattack, torch, flair


def test_word_swap_change_location():
    from flair.data import Sentence
    from flair.models import SequenceTagger

    from textattack.augmentation import Augmenter
    from textattack.transformations.word_swaps import WordSwapChangeLocation

    augmenter = Augmenter(transformation=WordSwapChangeLocation())
    s = "I am in Dallas."
    s_augmented = augmenter.augment(s)
    augmented_text = Sentence(s_augmented[0])
    tagger = SequenceTagger.load("flair/ner-english")
    original_text = Sentence(s)
    tagger.predict(original_text)
    tagger.predict(augmented_text)

    entity_original = []
    entity_augmented = []

    for entity in original_text.get_spans("ner"):
        entity_original.append(entity.tag)
    for entity in augmented_text.get_spans("ner"):
        entity_augmented.append(entity.tag)
    assert entity_original == entity_augmented


def test_word_swap_change_name():
    from flair.data import Sentence
    from flair.models import SequenceTagger

    from textattack.augmentation import Augmenter
    from textattack.transformations.word_swaps import WordSwapChangeName

    augmenter = Augmenter(transformation=WordSwapChangeName())
    s = "My name is Anthony Davis."
    s_augmented = augmenter.augment(s)
    augmented_text = Sentence(s_augmented[0])
    tagger = SequenceTagger.load("flair/ner-english")
    original_text = Sentence(s)
    tagger.predict(original_text)
    tagger.predict(augmented_text)

    entity_original = []
    entity_augmented = []

    for entity in original_text.get_spans("ner"):
        entity_original.append(entity.tag)
    for entity in augmented_text.get_spans("ner"):
        entity_augmented.append(entity.tag)
    assert entity_original == entity_augmented


def test_chinese_homophone_character_swap():
    from textattack.augmentation import Augmenter
    from textattack.transformations.word_swaps.chn_transformations import (
        ChineseHomophoneCharacterSwap,
    )

    augmenter = Augmenter(
        transformation=ChineseHomophoneCharacterSwap(),
        pct_words_to_swap=0.1,
        transformations_per_example=5,
        fast_augment=True,
    )
    s = "听见树林的呢喃，发现溪流中的知识。"
    augmented_text_list = augmenter.augment(s)
    augmented_s = "听见书林的呢喃，发现溪流中的知识。"
    assert augmented_s in augmented_text_list


def test_chinese_morphonym_character_swap():
    from textattack.augmentation import Augmenter
    from textattack.transformations.word_swaps.chn_transformations import (
        ChineseMorphonymCharacterSwap,
    )

    augmenter = Augmenter(
        transformation=ChineseMorphonymCharacterSwap(),
        pct_words_to_swap=0.1,
        transformations_per_example=5,
        fast_augment=True,
    )
    s = "听见树林的呢喃，发现溪流中的知识。"
    augmented_text_list = augmenter.augment(s)
    augmented_s = "听见树林的呢喃，发现溪流中的知枳。"
    assert augmented_s in augmented_text_list


def test_chinese_word_swap_hownet():
    from textattack.augmentation import Augmenter
    from textattack.transformations.word_swaps.chn_transformations import (
        ChineseWordSwapHowNet,
    )

    augmenter = Augmenter(
        transformation=ChineseWordSwapHowNet(),
        pct_words_to_swap=0.1,
        transformations_per_example=5,
        fast_augment=True,
    )
    s = "听见树林的呢喃，发现溪流中的知识。"
    augmented_text_list = augmenter.augment(s)
    augmented_s = "可见树林的呢喃，发现溪流中的知识。"
    assert augmented_s in augmented_text_list


def test_chinese_word_swap_masked():
    from textattack.augmentation import Augmenter
    from textattack.transformations.word_swaps.chn_transformations import (
        ChineseWordSwapMaskedLM,
    )

    augmenter = Augmenter(
        transformation=ChineseWordSwapMaskedLM(),
        pct_words_to_swap=0.1,
        transformations_per_example=5,
        fast_augment=True,
    )
    s = "听见树林的呢喃，发现溪流中的知识。"
    augmented_text_list = augmenter.augment(s)
    augmented_s = "听见树林的呢喃，了解溪流中的知识。"
    assert augmented_s in augmented_text_list
