"""Class for tk sample."""


class Logic:
    """Performs logic."""

    def logic_analyze(self, new):
        """
        Check len.

        :param new: some text
        :param return: if length if text > 10 True else False
        """
        if len(new) > 10:
            return False
        else:
            return True

    def logic_insert_func(self, obj, pos, text):
        """
        Insert in obj text in pos.

        :param obj: put text in this obj
        :param pos: where to insert (position)
        :param text: some text
        """
        obj.insert(pos, text)

    def logic_label(self, obj, text):
        """
        Set text in obj.

        :param obj: object where to insert
        :param text: some text
        """
        obj.set(text)
