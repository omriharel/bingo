#!/usr/bin/env python
# -*- coding: utf-8 -*-

import jinja2
import io
import random
import pprint

words = [
    u'שלום',
    u'מלחמה',
    u'לייצג',
    u'עוטף עזה',
    u'ימין',
    u'תל אביב',
    u'שוויון',
    u'אירוויזיון',
    u'תקווה',
    u'צה"ל',
    u'דמוקרטית',
    u'אלפיים',
    u'דונלד טראמפ',
    u'כבוד הכנסת',
    u'רמטכ"ל',
    u'ערבי',
    u'שגרירינו',
    u'יחד',
    u'נשיא המדינה',
    u'אסיר ציון',
    u'צוואר',
    u'הללויה',
    u'נתינה',
    u'שוויון',
    u'מפולגים',
    u'בתי המשפט',
    u'תהליכים',
    u'חיל אויר',
    u'מתרגש',
    u'נפעם',
    u'מצות',
    u'ממשלה',
    u'קואליציה',
    u'מלוכדים',
    u'יד',
    u'משקוף',
    u'מטרות',
    u'טרור',
    u'חמאס',
    u'ירושלים',
    u'שמיים',
    u'יעקב',
    u'זית',
    u'סטארט-אפ',
    u'ריבונות',
    u'נטל',
    u'גבולות',
    u'עורף',
    u'נושבות',
    u'צעדים',
    u'קדימה',
]


center_words = [
    u'אחדות',
    u'ממלכתיות',
    u'סייבר',
]


num_tables = 24
table_width = 5
table_height = 5
table_center = ((table_height - 1) / 2, (table_width -1 ) / 2)


def generate_bingo_data():
    tables = []

    for _ in xrange(num_tables):
        table = []
        included_words = {}

        for row_idx in xrange(table_height):
            row = []

            for col_idx in xrange(table_width):
                if (row_idx, col_idx) == table_center:
                    row.append(u'<span class="centerword">{0}</span>'.format(
                        random.choice(center_words)
                    ))
                else:
                    chosen_word = random.choice(words)

                    while chosen_word in included_words:
                        chosen_word = random.choice(words)

                    included_words[chosen_word] = True
                    row.append(chosen_word)

            table.append(row)

        tables.append(table)

    return tables



def main():
    jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader('.'))

    template = jinja_env.get_template('template.tpl.html')

    data = generate_bingo_data()

    written_template = template.render(data=data)

    print '--------------------------'
    print 'Template:'
    print written_template

    with io.open('output.html', 'w', encoding='utf-8') as f:
        f.write(written_template)

    print '--------------------------'


if __name__ == '__main__':
    main()
