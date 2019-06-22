---
layout:     post
title:      "Working with ansible - Pitfalls"
subtitle:   "Issues and common pitfalls while working with ansible"
date:       2017-03-17
author:     "Om Prakash Singh"
alias:      ['issues/ansible']
---

## Pitfall 1

lib/python3.5/site-packages/Crypto/Util/number.py:57: PowmInsecureWarning: Not using mpz_powm_sec.  You should rebuild using libgmp >= 5 to avoid timing attack vulnerability.

Lib GMP is GNU multiple precision arithmentic library.

download and follow the steps as below.

1. Need to get the development tools installed on to the system.

yum -y group-install "Development Tools"

yum -y install gcc libgcc glibs libffi-devel libxml2-devel libxslt-devel openssl-devel zlib-devel bzip2-devel ncurses-devel

2. Download the gmp libraries from its download site.
https://gmplib.org/#DOWNLOAD

3. compile and install.
tar -xvjpf gmp-versionno.tar.bz2
cd gmp-versionno/
./configure
make
make check
make install

4. one gmp installed rebuild your python PyCrypto
pip install --ignore-installed PyCrypto


## pitfall 2


devopsmain | UNREACHABLE! => {
    "changed": false,
    "msg": "Authentication failed.",
    "unreachable": true
}


Though the host is reachable it says unreachable, the fix is to add the entry for the same in /etc/hosts file or let your dns tell ansible where the host is.

