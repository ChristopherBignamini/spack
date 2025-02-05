# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class PyFrozenlist(PythonPackage):
    """A list-like structure which implements collections.abc.MutableSequence."""

    homepage = "https://github.com/aio-libs/frozenlist"
    pypi     = "frozenlist/frozenlist-1.2.0.tar.gz"

    version('1.2.0', sha256='68201be60ac56aff972dc18085800b6ee07973c49103a8aba669dee3d71079de')

    depends_on('python@3.6:', type=('build', 'run'))
    depends_on('py-setuptools', type='build')
