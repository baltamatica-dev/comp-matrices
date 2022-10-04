import re


# 定位匹配用 RE
re_dict = {
    '内核': re.compile(r'\[\*] 内核提供的命令：\n'),
    '脚本': re.compile(r'\[\*] 脚本提供的命令：\n'),
    '插件': re.compile(r'\[\*] 插件 \[(?P<plugin_list>[^]]+)] 提供的命令：\n'),
}  # re_dict


def parse_line(line: str):
    """使用 RE 匹配一行.
    """
    for key, rx in re_dict.items():
        match = rx.search(line)
        if match:
            return key, match

    # 无匹配, 返回 (None, None)
    return None, None


def parse_func_list(line: str):
    """解析函数列表.
    目前的函数列表使用 `\t` 分割
    """
    flist = line.strip().split('\t')
    return flist


def parse_help_file(file_path: str):
    """解析 `help` 命令输出的信息.
    """
    parse_mode = ''
    func_group = {}
    with open(file_path, 'r', encoding='UTF-8') as file_obj:
        line = file_obj.readline()
        while line:
            key, match = parse_line(line)

            if key == '内核':
                parse_mode = key
                line = file_obj.readline()
                flist = parse_func_list(line)
                func_group[parse_mode] = flist
                # print(f'[kernel func] {flist}')

            if key == '脚本':
                parse_mode = key
                line = file_obj.readline()
                flist = parse_func_list(line)
                func_group[parse_mode] = flist
                # print(f'[script func] {flist}')

            if key == '插件':
                parse_mode = key
                plugin_list = match.group('plugin_list')
                print(f'plugin_list={plugin_list}')
                line = file_obj.readline()
                flist = parse_func_list(line)
                func_group[parse_mode] = flist
                # print(f'[plugin func] {flist}')

            line = file_obj.readline()
        # -- while line
    # -- with open() as file_object

    return func_group


if __name__ == '__main__':
    file_full_path = 'help.txt'
    data = parse_help_file(file_full_path)
    print(data)
