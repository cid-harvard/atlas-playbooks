atlas-playbooks
===============
Ansible playbooks and Vagrantfile for the Atlas of Economic Complexity.

To install a dev environment from scratch:
- Get Virtualbox: https://www.virtualbox.org/wiki/Downloads
- Get Vagrant: http://www.vagrantup.com/downloads.html
- Install ansible globally with `sudo pip install ansible` (or use easy_install instead of pip).
- Run `git clone https://github.com/makmanalp/atlas-playbooks && cd atlas-playbooks && vagrant up`
- Sit back and wait till all the stuff downloads. It'll download a 350mb VM image, around that much more for all the required python and ubuntu packages.
