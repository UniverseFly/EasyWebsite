# -*- coding: utf-8 -*-
from markdown.extensions import Extension


class MathExtension(Extension):
    def __init__(self, *args, **kwargs):
        super(MathExtension, self).__init__(*args, **kwargs)

    def extendMarkdown(self, md):
        md.ESCAPED_CHARS = []


def makeExtension(*args, **kwargs):
    return MathExtension(*args, **kwargs)