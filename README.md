# ansible_get_playbook_name_plugin
## get ansible-playbook name (unix-like systems)

1. `pip(3) install -r requirements.txt`
2. `ansible-playbook get_playbook_name.yml` OR `ansible-playbook playbook_name.yml`

First playbook uses built-in functions and returns the name of the playbook executed  
The second one playbook uses filter_plugin to get the same result
