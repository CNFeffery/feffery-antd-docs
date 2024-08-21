import re
import sys
import feffery_antd_components as fac


def export_api_document(module_name):
    module_doc = getattr(fac, module_name).__doc__
    with open(
        f'./public/api_documents/en_us/{module_name}.md', 'w', encoding='utf-8'
    ) as md_file:
        md_file.write(
            re.sub(
                '^.*?Keyword arguments\:',
                '',
                module_doc,
                flags=re.S,
            )
        )


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python export_api_document.py <component_name>')
    else:
        module_name = sys.argv[1]
        export_api_document(module_name)
        print(f"{module_name}'s __doc__ exported successfully!")
