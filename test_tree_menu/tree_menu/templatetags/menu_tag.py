from django import template
from ..models import Menu, TreeMenu

register = template.Library()


@register.inclusion_tag('tree_menu/menu.html')
def menu_tag(name: str = None):
    menu = Menu.objects.filter(title=name).first()
    tree = TreeMenu.objects.raw(f'''
    WITH RECURSIVE tree AS (
          SELECT id, title, parent_id, 1 as lvl
          FROM TreeMenu
          WHERE parent_id = {menu.pk}
        UNION all
          SELECT tk.id, tk.title, tk.parent_id, t.lvl+1 as lvl
          FROM TreeMenu AS tk, tree AS t
          WHERE tk.id = t.parent_id
        )
    SELECT * FROM tree
    ''')
    print(tree)
    for item in tree:
        print(item.title, item.lvl)
    return {tree}