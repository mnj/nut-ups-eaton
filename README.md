# nut-ups-eaton
Custom net-snmpd script to pass NUT Eaton UPS information to Librenms

The built-in app for NUT ups in LibreNMS is missing alot of information I would like to graph, so decided to create this workaround.

Requirements:
- Python3:
    - snmp_passpersist (`python3 -m pip install snmp_passpersist`)
- Net-SNMP
- LibreNMS
