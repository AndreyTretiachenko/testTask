from django import template
from ..models import Menu, TreeMenu

register = template.Library()


@register.inclusion_tag('tree_menu/menu.html')
def menu_tag(name: str = None):
    tree = TreeMenu.objects.raw(f'''
    WITH RECURSIVE tree AS (
          SELECT id, title, parent_id, 1 as lvl
          FROM TreeMenu
          WHERE parent_id = (
            select id from TreeMenu where is_root = True AND menu_id = (
                select id from tree_menu_menu where title = '{name}')
          )
        UNION
          SELECT tk.id, tk.title, tk.parent_id, t.lvl+1 as lvl
          FROM TreeMenu AS tk, tree AS t
          WHERE t.id = tk.parent_id
        )
    SELECT * FROM tree
    ''')

    return {}