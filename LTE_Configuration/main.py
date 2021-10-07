import paramiko

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('192.168.127.100', username='admin', password="0001mpnt", look_for_keys=False)
stdin, stdout, stderr = client.exec_command('interface bridge add name=bridge1')
stdin, stdout, stderr = client.exec_command('interface bridge port add bridge=bridge1 interface=ether1')
stdin, stdout, stderr = client.exec_command('interface bridge port add bridge=bridge1 interface=ether2')
stdin, stdout, stderr = client.exec_command('interface bridge port add bridge=bridge1 interface=ether3')
stdin, stdout, stderr = client.exec_command('ip address add address=192.168.127.100/24 interface=bridge1')
stdin, stdout, stderr = client.exec_command('ip dhcp-client add interface=lte1 use-peer-dns=yes add-default-route=yes disabled=no')
stdin, stdout, stderr = client.exec_command('ip firewall nat add chain=srcnat out-interface=lte1 action=masquerade')
stdin, stdout, stderr = client.exec_command('interface lte set lte1 allow-roaming=yes')
stdin, stdout, stderr = client.exec_command('interface lte apn add name=GSTEL apn=rh')
stdin, stdout, stderr = client.exec_command('interface lte apn add name=roaming apn=internet user=web password=web authentication=chap')
stdin, stdout, stderr = client.exec_command('interface lte set lte1 apn-profiles=GSTEL')
stdin, stdout, stderr = client.exec_command('tool romon set enabled=yes secret=mpnt')
stdin, stdout, stderr = client.exec_command('system identity set name="LTE"')
stdin, stdout, stderr = client.exec_command('password old-password="" new-password="0001mpnt" confirm-new-password="0001mpnt"')
stdin, stdout, stderr = client.exec_command('ip address remove [find interface="ether1"]')
for line in stdout:
    print(line.strip('\n')) 
client.close()
