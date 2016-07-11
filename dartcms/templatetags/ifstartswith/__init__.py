# coding: utf-8
from django import template
from django.template import Node, Variable, NodeList, VariableDoesNotExist


def do_startswith(parser, token, negate):
    try:
        tag_name, string, start_string = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError, "%r tag requires two arguments" % token.contents.split()[0]
    end_tag = 'end' + tag_name
    nodelist_true = parser.parse(('else', end_tag))
    token = parser.next_token()
    if token.contents == 'else':
        nodelist_false = parser.parse((end_tag,))
        parser.delete_first_token()
    else:
        nodelist_false = NodeList()
    return IfStartsWithNode(string, start_string, nodelist_true, nodelist_false, negate)


class IfStartsWithNode(Node):
    def __init__(self, string, start_string, nodelist_true, nodelist_false, negate):
        self.start_string, self.string = Variable(start_string), Variable(string)
        self.nodelist_true, self.nodelist_false = nodelist_true, nodelist_false
        self.negate = negate
        self.negate = negate

    def __repr__(self):
        return "<IfStartsWithNode>"

    def render(self, context):
        try:
            string = self.string.resolve(context)
        except VariableDoesNotExist:
            string = None
        try:
            start_string = self.start_string.resolve(context)
        except VariableDoesNotExist:
            start_string = None

        if (self.negate and not string.startswith(start_string)) or (
                not self.negate and string.startswith(start_string)):
            return self.nodelist_true.render(context)
        return self.nodelist_false.render(context)