class Logger:
    def __init__(self):
        self.commands = []

    def append_command(self, command):
        self.commands.append(command)

    def write_to_file(self):
        fname = 'out.txt'

        with open(fname, 'w') as f:
            f.write('{}'.format(len(self.commands)))
            for cmd in commands:
                cmd_name = cmd['name']
                if cmd_name == 'load':
                    f.write('FIXME:{} L {} {} {}'.format(cmd['drone_id'],
                                                         cmd['warehouse_id'],
                                                         cmd['prod_id'],
                                                         cmd['prod_count']))
                elif cmd_name == 'deliver':
                    f.write('FIXME:{} L {} {} {}'.format(cmd['drone_id'],
                                                         cmd['order_id'],
                                                         cmd['prod_id'],
                                                         cmd['prod_count']))

