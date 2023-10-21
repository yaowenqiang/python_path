from icecream import ic
"""
    cut large text into equal length lines without word-breaking
"""
def wrap(text, line_length):
    # assert line_length > 0, 'line_length must b positive'"
    if line_length < 1:
        raise ValueError(f'line_length {line_length} is not positive')
    words = text.split()
    max_word_length = max(map(len, words))
    if max_word_length > line_length:
        err_msg = f"line_length must be at least as long as the longest word's length {max_word_length}"
        err_msg1 = f'line_length must be at least as long as the longest word''s length {max_word_length}'
        ic(err_msg1)
        raise ValueError(err_msg)
    lines_of_words = []
    current_line_length = line_length
    for word in words:
        if current_line_length + len(word) > line_length:
            lines_of_words.append([])
            current_line_length = 0
        lines_of_words[-1].append(word)
        current_line_length += len(word) + len(' ')

    lines = [' '.join(line_of_words) for line_of_words in lines_of_words]
    result = '\n'.join(lines)
    assert all(len(line) <= line_length for line in result.splitlines())
    return result


if __name__ == '__main__':
    wealth_of_nations = 'The annual labour of every nation is the fund which or' \
            'iginally supplies it with all the necessaries and conveniences of life wh' \
            'ich it annually consumes, and which consist always either in the immediate' \
            'produce of that labour, or in what is purchased with that produce from other ' \
            'nations. According therefore as this produce, or what is purchased with it, be' \
            'ars a greater or smaller proportion to the number of those who are to consume it' \
            ', the nation will be better or worse supplied with all the necessaries and convenie' \
            'nces for which it has occasion. But this proportion must in every nation be regulated' \
            'by two different circumstances; first, by the skill, dexterity, and judgment with which ' \
            'its labour is generally applied; and, secondly, by the proportion between the number of ' \
            'those who are employed in useful labour, and that of those who are not so employed. Whate' \
            'ver be the soil, climate, or extent of territory of any particular nation, the abundance ' \
            'or scantiness of its annual supply must, in that particular situation, depend upon those two '\
            'circumstances. The abundance or scantiness of this supply, too, seems to depend more upon the '\
            'former of those two circumstances than upon the latter. Among the savage nations of hunters and '\
            'fishers, every individual who is able to work, is more or less employed in useful labour, and endea'\
            'vours to provide, as well as he can, the necessaries and conveniences of life, for himself, or such '\
            'of his family or tribe as are either too old, or too young, or too infirm to go a hunting and fishing. ' \
            'Such nations, however, are so miserably poor that, from mere want, they are frequently reduced, or, at ' \
            'least, think themselves reduced, to the necessity sometimes of directly destroying, and sometimes of aband' \
            'oning their infants, their old people, and those afflicted with lingering diseases, to perish with hunger, or ' \
            'to be devoured by wild beasts. Among civilised and thriving nations, on the contrary, though a great number of ' \
            'people do not labour at all, many of whom consume the produce of ten times, frequently of a hundred times more lab' \
            'our than the greater part of those who work; yet the produce of the whole labour of the society is so great that all a' \
            're often abundantly supplied, and a workman, even of the lowest and poorest order, if he is frugal and industrious, may en' \
            'joy a greater share of the necessaries and conveniences of life than it is possible for any savage to acquire. The causes of ' \
            'this improvement, in the productive powers of labour, and the order, according to which its produce is naturally distributed among ' \
            'the different ranks and conditions of men in the society, make the subject of the first book of this Inquiry. Whatever be the actual sta' \
            'te of the skill, dexterity, and judgment with which labour is applied in any nation, the abundance or scantiness of its annual supply must ' \
            'depend, during the continuance of that state, upon the proportion between the number of those who are annually employed in useful labour, and ' \
            'that of those who are not so employed. The number of useful and productive labourers, it will hereafter appear, is everywhere in proportion to the ' \
            'quantity of capital stock which is employed in setting them to work, and to the particular way in which it is so employed. The second book, therefore, ' \
            'treats of the nature of capital stock, of the manner in which it is gradually accumulated, and of the different quantities of labour which it puts into mot' \
            'ion, according to the different ways in which it is employed. Nations tolerably well advanced as to skill, dexterity, and judgment, in the application of labou' \
            'r, have followed very different plans in the general conduct or direction of it; those plans have not all been equally favourable to the greatness of its produce. ' \
            'The policy of some nations has given extraordinary encouragement to the industry of the country; that of others to the industry of towns. Scarce any nation has dealt ' \
            'equally and impartially with every sort of industry. Since the downfall of the Roman empire, the policy of Europe has been more favourable to arts, manufactures, and comm' \
            'erce, the industry of towns, than to agriculture, the industry of the country. The circumstances which seem to have introduced and established this policy are explained in th' \
            'e third book. Though those different plans were, perhaps, first introduced by the private interests and prejudices of particular orders of men, without any regard to, or foresight ' \
            'of, their consequences upon the general welfare of the society; yet they have given occasion to very different theories of political economy; of which some magnify the importance of th' \
            'at industry which is carried on in towns, others of that which is carried on in the country. Those theories have had a considerable influence, not only upon the opinions of men of learning, ' \
            'but upon the public conduct of princes and sovereign states. I have endeavoured, in the fourth book, to explain, as fully and distinctly as I can, those different theories, and the principal ef' \
            'fects which they have produced in different ages and nations. To explain in what has consisted the revenue of the great body of the people, or what has been the nature of those funds which, in diff' \
            'erent ages and nations, have supplied their annual consumption, is the object of these four first books. The fifth and last book treats of the revenue of the sovereign, or commonwealth. In this book I ha' \
            've endeavoured to show, first, what are the necessary expenses of the sovereign, or commonwealth; which of those expenses ought to be defrayed by the general contribution of the whole society; and which of ' \
            'them by that of some particular part only, or of some particular members of it: secondly, what are the different methods in which the whole society may be made to contribute towards defraying the expenses incu' \
            'mbent on the whole society, and what are the principal advantages and inconveniences of each of those methods: and, thirdly and lastly, what are the reasons and causes which have induced almost all modern governme' \
            'nts to mortgage some part of this revenue, or to contract debts, and what have been the effects of those debts upon the real wealth, the annual produce of the land and labour of the society.'
    print(wrap(wealth_of_nations, 16))