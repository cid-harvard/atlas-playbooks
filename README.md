atlas-playbooks
===============

Ansible playbooks and Vagrantfile for the Atlas of Economic Complexity.

Setting Up a Development Environment
------------------------------------

To easily install a dev environment from scratch:
- Get Virtualbox: https://www.virtualbox.org/wiki/Downloads
- Get Vagrant: http://www.vagrantup.com/downloads.html
- Install ansible globally with `sudo pip install ansible` (or use easy_install instead of pip).
- Double check that the installs worked by running `ansible` and `vagrant` in the command line.
- Run `git clone https://github.com/makmanalp/atlas-playbooks && cd atlas-playbooks && vagrant up`
- Sit back and wait till all the stuff downloads. It'll download a 350mb VM
  image, around that much more for all the required python and ubuntu packages.
  Should take around 10 minutes.

Usage Info
---------
- There are two shared directories with the VM. Any change made within the VM
  reflects to the outside of the VM, and vice versa.
    * `vagrant_shared/`: For moving over large SQL dumps etc.
    * `atlas/`: Contains the main source for the site, a checkout of the
      observatory_economic_complexity repo. You can code on this.
- Run "vagrant ssh" to get into the box.
- There are also port forwards for the services running inside the VM.
    * 8080: main HTTP server
    * 3307: mysql

So for example: http://localhost:8080/ should get to the Django server in the vm.
