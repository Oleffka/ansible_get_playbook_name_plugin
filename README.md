# ansible_get_playbook_name_plugin  
## get ansible-playbook name (unix-like systems)  

1. `pip(3) install -r requirements.txt`  
2. `ansible-playbook playbook_name.yml` returns the name of the playbook executed (works on linux)  

### plugins  
#### filter plugin  
`ansible-playbook get_playbook_name_fp.yml` returns the name of the playbook, needs something like 'None' as input  

#### filter plugin  
`ansible-playbook get_playbook_name_lp.yml` does the same (w/o any input), uses lookup built-in function
