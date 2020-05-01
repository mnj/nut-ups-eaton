# nut-ups-eaton
Custom net-snmp extend script to pass NUT information for a Eaton UPS to Librenms, it is generic though, as long as upcs returns the ups information.

The built-in app for NUT ups in LibreNMS is missing alot of information I would like to graph, so decided to create this workaround.

Requirements:
- Python (>=3.7)
- Net-SNMP
- LibreNMS

Copy the eaton-nut.py script to /etc/snmpd/eaton-nut.py
chmod a+x /etc/snmpd/eaton-nut.py

Add the following to /etc/snmp/snmpd.conf:
extend eaton-nut /etc/snmp/eaton-nut.py names
extend eaton-nut /etc/snmp/eaton-nut.py values

Relead the snmpd daemon.
