
def generate_shortcut_panel_data(raw_menu_items):
    """基于侧边菜单栏数据结构推导搜索面板数据结构

    Args:
        raw_menu_items (_type_): 输入的侧边菜单栏数据结构
    """

    output_data = []

    # “快速入门”
    output_data.extend(
        [
            {
                'id': item['props']['key'],
                'title': item['props']['title'],
                'section': '快速入门',
                'handler': '() => window.open("%s")' % item['props']['href'],
            }
            for item in raw_menu_items[0]['children']
        ]
    )

    # “组件介绍”
    for level1 in raw_menu_items[2]['children']:
        for level2 in level1['children']:
            # 若为常规菜单项
            if level2['component'] == 'Item':
                output_data.append(
                    {
                        'id': level2['props']['key'],
                        'title': level2['props']['title'],
                        'section': '组件介绍',
                        'handler': '() => window.open("%s")' % level2['props']['href'],
                    }
                )
            # 否则进行展开
            elif level2['component'] == 'SubMenu':
                for level3 in level2['children']:
                    if 'table' in level3['props']['key'].lower():
                        output_data.append(
                            {
                                'id': level3['props']['key'],
                                'title': 'AntdTable '+level3['props']['title'],
                                'section': '组件介绍',
                                'handler': '() => window.open("%s")' % level3['props']['href'],
                            }
                        )
                    else:
                        output_data.append(
                            {
                                'id': level3['props']['key'],
                                'title': level3['props']['title'],
                                'section': '组件介绍',
                                'handler': '() => window.open("%s")' % level3['props']['href'],
                            }
                        )

    # “进阶使用”
    output_data.extend(
        [
            {
                'id': item['props']['key'],
                'title': item['props']['title'],
                'section': '进阶使用',
                'handler': '() => window.open("%s")' % item['props']['href'],
            }
            for item in raw_menu_items[4]['children']
        ]
    )

    return output_data
