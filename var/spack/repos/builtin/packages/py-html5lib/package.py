# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyHtml5lib(PythonPackage):
    """HTML parser based on the WHATWG HTML specification."""

    homepage = "https://github.com/html5lib/html5lib-python"
    url      = "https://pypi.io/packages/source/h/html5lib/html5lib-0.9999999.tar.gz"

    version('1.0.1', '66cb0dcfdbbc4f9c3ba1a63fdb511ffdbd4f513b2b6d81b80cd26ce6b3fb3736')
    version('0.9999999', 'ef43cb05e9e799f25d65d1135838a96f')

    depends_on('python@2.6:2.8,3.2:', when='@0.9999999', type=('build', 'run'))
    depends_on('python@2.6:2.8,3.3:', when='@1.0.1:', type=('build', 'run'))
    depends_on('py-six', type=('build', 'run'))
    depends_on('py-six@1.9:', type=('build', 'run'), when='@1.0.1:')
    depends_on('py-setuptools', type='build', when='@1.0.1:')
    depends_on('py-webencodings', type=('build', 'run'), when='@1.0.1:')
