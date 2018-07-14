from winrm.protocol import Protocol

p = Protocol(
    endpoint='http://<host fqdn>:5985/wsman',
    transport='ntlm',
    username='',
    password='',
    server_cert_validation='ignore')
shell_id = p.open_shell()
#command_id = p.run_command(shell_id, 'ipconfig', ['/all'])
command_id = p.run_command(shell_id, 'powershell', ['$PSVersionTable'])
std_out, std_err, status_code = p.get_command_output(shell_id, command_id)
print(std_out)
p.cleanup_command(shell_id, command_id)
p.close_shell(shell_id)
