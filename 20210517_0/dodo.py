def task_png():
    """Create png file."""
    return {
            "file_dep": ["pct.dia"],
            "actions": ["dia pct.dia -e pct.png"],
            "targets": ["pct.png"],
    }


def task_icon():
    """Create icon file."""
    return {
            "file_dep": ["pct.png"],
            "actions": ["convert pct.png -resize 64 pct-icon.png"],
            "targets": ["pct-icon.png"],
    }

def task_remove():
    """Remove all junk."""
    return {
            "actions": ["rm -f *.png *~"],
    }


