atlas-playbooks
===============

Ansible playbooks and Vagrantfile for the Atlas of Economic Complexity.

Setting Up a Development Environment
------------------------------------

To easily install a virtualized dev environment from scratch:

1. Install pre-requirements (5 min):
  - **Virtualbox**: https://www.virtualbox.org/wiki/Downloads . Virtualbox lets
  you run virtual computers on top of your actual one that you can run a
  separate operating system on, allowing you to install the atlas in its own
  contained environment instead of polluting your computer.
  - **Vagrant**: http://www.vagrantup.com/downloads.html . Vagrant lets you
  create, automate, tear down and manage virtualized environments (that run on Virtualbox).
  - **Ansible**: Install ansible globally with `sudo pip install ansible` (or use easy_install
  instead of pip). Ansible automates installation of software packages and
  creation of configuration files, so you don’t have to manually install
  all the little components that are required to get the atlas to work.
  - **Double check** that the installs worked by running `ansible` and `vagrant` in
  the command line, and by running virtualbox.

2. Clone the code (30s):
  - Run `git clone https://github.com/makmanalp/atlas-playbooks && cd atlas-playbooks`

3. Make sure you have the data (30s - 5min):
  - Put a bzip-compressed atlas db dump into the vagrant_shared directory and
  name it atlas_dump.sql.bz2.

4. Begin installing (30min)
  - Do `vagrant up`. Sit back and wait until all the stuff downloads. It'll download a 350mb VM
  image, around that much more for all the required python and ubuntu packages.
  The “importing atlas DB” part takes the longest.

5. Test it out!
  - Run `vagrant ssh` to get in, then `cd /srv/atlas/` and `source
  env/bin/activate` to get into the virtualenv. Then go in `django_files` and
  run `manage.py runserver 0.0.0.0:8000`. The 0.0.0.0 is important to get
  django to answer requests that come from outside the VM.
  - Go to http://127.0.0.1:8000/ with your browser on the outside.

Basic Usage
-----------
- Run “vagrant up” to start the box, "vagrant ssh" to get into the box,
  "vagrant suspend" to save the state of the box (akin to “hibernate”) and
  “vagrant halt” to stop it completely.
- There are two shared directories with the VM. Any change made within the VM
  reflects to the outside of the VM, and vice versa.
    * `vagrant_shared/`: For moving over large SQL dumps etc.
    * `atlas/`: Contains the main source for the site, a checkout of the
      atlas-economic-complexity repo. You can write / edit code on this. Inside
      the box, this maps to the /srv/atlas directory.
- The usual development process involves working with your editor on the
  “atlas” directory outside the VM and have those changes reflected
  automatically to the inside. You ssh in to stop / start the server processes.
  If you’re going to make configuration changes, it might make sense to add
  them to the ansible playbooks instead of manually doing them if you want to
  preserve those changes and have them reflected across all installations.

More Info
---------
- Run “git pull” to get the latest version of the playbooks from git, and then "vagrant provision” to get vagrant to do all the new installation / configuration needed.
- Run "vagrant destroy" and then “vagrant up” to get a fresh reinstallation.
- Run "vagrant help" for more info on how to stop, start, reload, destroy the virtual box.
- An ansible.cfg is already set up so you can do `ansible default -m ping` or `ansible-playbook playbook.yml` (which is what `vagrant provision` does)
- If you want to make ansible do more stuff, check out the ansible module index: http://docs.ansible.com/modules_by_category.html
- There are also port forwards for the services running inside the VM.
    * 8000: main HTTP server
    * 3307: mysql
    * 6379: redis
    * 9200: elasticsearch

<!--
- Make sure you have an ssh-agent running (check with `ps aux | grep
  ssh-agent`) and add your github ssh key with `ssh-add ~/.ssh/key_name.rsa`.
  Ssh-agent lets you use your local ssh keys in the remote server. This allows
  you to do a “git clone” on the virtual box even though your ssh keys are not
  there. To learn more about ssh-agent, read this guide
  (https://help.github.com/articles/using-ssh-agent-forwarding)
  -->
