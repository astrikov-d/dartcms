# -*- coding: utf-8 -*-
import math

from django.core.paginator import Paginator, QuerySetPaginator, Page, InvalidPage

__all__ = (
    'InvalidPage',
    'ExPaginator',
    'DiggPaginator',
    'QuerySetDiggPaginator',
)


class ExPaginator(Paginator):
    def _ensure_int(self, num, e):
        try:
            return int(num)
        except ValueError:
            raise e

    def page(self, number, softlimit=False):
        try:
            return super(ExPaginator, self).page(number)
        except InvalidPage, e:
            number = self._ensure_int(number, e)
            if number > self.num_pages and softlimit:
                return self.page(self.num_pages, softlimit=False)
            else:
                raise e


class DiggPaginator(ExPaginator):
    def __init__(self, *args, **kwargs):
        self.body = kwargs.pop('body', 10)
        self.tail = kwargs.pop('tail', 2)
        self.align_left = kwargs.pop('align_left', False)
        self.margin = kwargs.pop('margin', 4)

        max_padding = int(math.ceil(self.body / 2.0) - 1)
        self.padding = kwargs.pop('padding', min(4, max_padding))
        if self.padding > max_padding:
            raise ValueError('padding too large for body (max %d)' % max_padding)
        super(DiggPaginator, self).__init__(*args, **kwargs)

    def page(self, number, *args, **kwargs):
        page = super(DiggPaginator, self).page(number, *args, **kwargs)
        number = int(number)

        num_pages, body, tail, padding, margin = \
            self.num_pages, self.body, self.tail, self.padding, self.margin

        main_range = map(int, [
            math.floor(number - body / 2.0) + 1,
            math.floor(number + body / 2.0)])

        if main_range[0] < 1:
            main_range = map(abs(main_range[0] - 1).__add__, main_range)
        if main_range[1] > num_pages:
            main_range = map((num_pages - main_range[1]).__add__, main_range)

        if main_range[0] <= tail + margin:
            leading = []
            main_range = [1, max(body, min(number + padding, main_range[1]))]
            main_range[0] = 1
        else:
            leading = range(1, tail + 1)

        if self.align_left:
            trailing = []
        else:
            if main_range[1] >= num_pages - (tail + margin) + 1:
                trailing = []
                if not leading:
                    main_range = [1, num_pages]
                else:
                    main_range = [min(num_pages - body + 1, max(number - padding, main_range[0])), num_pages]
            else:
                trailing = range(num_pages - tail + 1, num_pages + 1)

        main_range = [max(main_range[0], 1), min(main_range[1], num_pages)]
        page.main_range = range(main_range[0], main_range[1] + 1)
        page.leading_range = leading
        page.trailing_range = trailing
        page.page_range = reduce(lambda x, y: x + ((x and y) and [False]) + y,
                                 [page.leading_range, page.main_range, page.trailing_range])

        page.__class__ = DiggPage
        return page


class DiggPage(Page):
    def __str__(self):
        return " ... ".join(filter(None, [
            " ".join(map(str, self.leading_range)),
            " ".join(map(str, self.main_range)),
            " ".join(map(str, self.trailing_range))]))


class QuerySetDiggPaginator(DiggPaginator, QuerySetPaginator):
    pass
