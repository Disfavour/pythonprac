"""Class for tk sample."""


class Logic:
    """Performs logic."""

    def logic_analyze(self, new):
        """Check len."""
        if len(new) > 10:
            return False
        else:
            return True

    def logic_insert_func(self, obj, pos, text):
        """Insert in obj text in pos."""
        obj.insert(pos, text)

    def logic_label(self, obj, text):
        """Set text in obj."""
        obj.set(text)
