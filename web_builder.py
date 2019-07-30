import os
import sys


def read_component_code(file_name):
    with open(file_name, 'r') as f:
        content = f.read()
        return content

def update_web_build(file_path, pre_text, component_code, post_text):
    with open(file_path, "w") as web_builder:
        for line in pre_text:
            web_builder.write(line)
            web_builder.write('\n')

        web_builder.write(component_code)
        web_builder.write('\n')

        for line in post_text:
            web_builder.write(line)
            web_builder.write('\n')

def list_rindex(li, x, count):
    if count == None:
        for i in reversed(range(len(li))):
            if str(li[i]).strip() == x:
                return i
        raise ValueError("{} is not in list".format(x))
    else:
        cnt = 1
        for i in reversed(range(len(li))):
            if str(li[i]).strip() == x:
                if cnt == count:
                    return i
                cnt += 1
        raise ValueError("{} is not in list".format(x))

def add_component(component_name, position):
    web_build_path = "web-builder/src/pages/index.js"
    component_code = ''

    templ_file_path = 'templates/{}_template.html'.format(component_name)
    if os.path.exists(templ_file_path):
        component_code = read_component_code(templ_file_path)
    
    with open(web_build_path, "r") as web_builder:
        lines = web_builder.read().splitlines()

        if component_name == 'card':
            split_idx = list_rindex(lines, "</div>", None)
        else:
            split_idx = list_rindex(lines, "</div>", 2)
        pre_text = lines[:split_idx]
        post_text = lines[split_idx:]


        update_web_build(web_build_path, pre_text, component_code, post_text)


if __name__ == '__main__':
    add_component('textbox','pos')
