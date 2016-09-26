from netmiko.cisco_base_connection import CiscoSSHConnection

class NetgearSSH(CiscoSSHConnection):

    def exit_config_mode(self, exit_config='exit'):
        """Exit config mode."""
        return super(NetgearSSH, self).exit_config_mode(exit_config=exit_config)

    def check_config_mode(self, check_string='(Config)', pattern=''):
        return super(NetgearSSH, self).check_config_mode(check_string=check_string, pattern=self.base_prompt)

    def config_mode(self, config_command='configure', pattern=''):
        return super(NetgearSSH, self).config_mode(config_command=config_command)

    def cleanup(self):
        self.exit_config_mode()
        self.write_channel("exit\n")