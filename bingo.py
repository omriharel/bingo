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
    u'חזית',
    u'ימין',
    u'תל אביב',
    u'שוויון',
    u'מכובדיי כולם',
    u'תקווה',
    u'צה"ל',
    u'דמוקרטית',
    u'אלפיים',
    u'הכנסת',
    u'רמטכ"ל',
    u'ערבי',
    u'שגרירינו',
    u'יחד',
    u'נשיא המדינה',
    u'המצב',
    u'חלב',
    u'אבטלה',
    u'ברכה',
    u'הללויה',
    u'נתינה',
    u'שוויון',
    u'מפולגים',
    u'בתי המשפט',
    u'תהליכים',
    u'חיל אוויר',
    u'חגיגי',
    u'מתרגש',
    u'ממשלה',
    u'קואליציה',
    u'טרור',
    u'ירושלים',
    u'קהל',
    u'זית',
    u'סטארט-אפ',
    u'ריבונות',
    u'נטל',
    u'גבולות',
    u'עורף',
    u'נושבות',
    u'צעדים',
    u'קדימה',
    u'ניצחון',
    u'משרד הבריאות',
    u'הצוותים הרפואיים',
    u'בזכות ולא בחסד',
    u'*דופק לגמרי את הביטוי*',
    u'*קורא את המילה עם דגש לא נכון*',
    u'*מגמגם*',
]


center_words = [
    u'קורונה',
]


num_tables = 1
copies = [
    u'עמרי',
    u'איגור',
    u'לב',
    u'הדר',
    u'נועם הבן',
    u'נועם הבת',
    u'אייל',
    u'אריאל',
    u'סהר',
    u'קובי',
    u'עופר',
]
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

    for recipient in copies:
        data = generate_bingo_data()

        written_template = template.render(data=data, recipient=recipient)

        with io.open(u'{0}.html'.format(recipient), 'w', encoding='utf-8') as f:
            f.write(written_template)


if __name__ == '__main__':
    main()
