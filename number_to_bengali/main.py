from .utils import (float_int_extraction, fraction_to_words, generate_segments,
                    generate_segments_for_year, input_sanitizer,
                    whole_part_word_gen, whole_part_word_gen_for_year)


def to_bn_word(number):
    """
    Takes a number and outputs the word form in Bengali for that number.
    """

    generated_words = ""
    number = input_sanitizer(number)

    whole, fraction = float_int_extraction(number)

    if number > 1100 and number<2000:
        whole_segments = generate_segments_for_year(whole)

        generated_words = whole_part_word_gen_for_year(whole_segments)

    else:
        whole_segments = generate_segments(whole)

        generated_words = whole_part_word_gen(whole_segments)

    if fraction:
        if generated_words:
            return generated_words + " দশমিক " + fraction_to_words(fraction)
        else:
            return "দশমিক " + fraction_to_words(fraction)
    else:
        return generated_words
