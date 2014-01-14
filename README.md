atlas-playbooks
===============

Setting Up a Development Environment
------------------------------------

Ansible playbooks and Vagrantfile for the Atlas of Economic Complexity.

To install a dev environment from scratch:
- Get Virtualbox: https://www.virtualbox.org/wiki/Downloads
- Get Vagrant: http://www.vagrantup.com/downloads.html
- Install ansible globally with `sudo pip install ansible` (or use easy_install instead of pip).
- Run `git clone https://github.com/makmanalp/atlas-playbooks && cd atlas-playbooks && vagrant up`
- Sit back and wait till all the stuff downloads. It'll download a 350mb VM
  image, around that much more for all the required python and ubuntu packages.

Usage Info
---------
- There are two shared directories with the VM. Any change made within the VM
  reflects to the outside of the VM, and vice versa.
    * `data/`: For moving over large SQL dumps etc.
    * `atlas/`: Contains the main source for the site, a checkout of the
      observatory_economic_complexity repo. You can code on this.
- Run "vagrant ssh" to get into the box.
- There are also port forwards for the services running inside the VM.
    * 8080: main HTTP server
    * 3307: mysql
  Example: http://localhost:8080/ should get to the django server in the vm.
