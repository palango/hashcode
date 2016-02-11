class Logger:
    def __init__(self):
        self.commands = {}

    def append_command(self, t, command):
        clist = self.commands[t]
        clist.append(command)
        self.commands[t] = clist

    def write_to_file(self, t_max):
        fname = 'out.txt'

        linear = []

        for t in range(t_max):
            if t in self.commands:
                linear.extend(self.commands[t])

        with open(fname, 'w') as f:
            f.write('{}'.format(len(self.commands)))
            for cmd in linear:
                cmd_name = cmd['name']
                if cmd_name == 'load':
                    f.write('{} L {} {} {}'.format(cmd['drone_id'],
                                                   cmd['warehouse_id'],
                                                   cmd['prod_id'],
                                                   cmd['prod_count']))
                elif cmd_name == 'deliver':
                    f.write('{} D {} {} {}'.format(cmd['drone_id'],
                                                   cmd['order_id'],
                                                   cmd['prod_id'],
                                                   cmd['prod_count']))
            f.flush()