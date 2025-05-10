

def cmd_format(command: dict):
    if command is None:
        return []

    cmd_list = []
    for k, v in command.items():
        if type(v) is bool:
            if v: cmd_list.append(f'--{k}')
            continue

        if v is None: continue

        cmd_list += [f'--{k}', v]

    return cmd_list