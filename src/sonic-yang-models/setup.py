import shutil
import os
import glob
import jinja2
from setuptools import setup, find_packages
from setuptools.command.build_py import build_py

# read me
with open('README.rst') as readme_file:
    readme = readme_file.read()

class my_build_py(build_py):
    def run(self):
        if not self.dry_run:
            print("hehe")

        if not os.path.exists("./yang-models"):
            os.makedirs("./yang-models")

        if not os.path.exists("./iyang-models"):
            os.makedirs("./iyang-models")

        # copy non-template yang model to internal yang model directory
        for fname in glob.glob("./yang-models/*.yang"):
            bfname = os.path.basename(fname)
            shutil.copyfile("./yang-models/{}".format(bfname), "./iyang-models/{}".format(bfname))

        # templated yang models
        env = jinja2.Environment(loader=jinja2.FileSystemLoader('./yang-templates/'), trim_blocks=True)
        for fname in glob.glob("./yang-templates/*.yang.j2"):
            bfname = os.path.basename(fname)
            template = env.get_template(bfname)
            yang_model = template.render(yang_model_type="ext")
            iyang_model = template.render(yang_model_type="int")
            with open("./yang-models/{}".format(bfname.strip(".j2")), 'w') as f:
                f.write(yang_model)
            with open("./iyang-models/{}".format(bfname.strip(".j2")), 'w') as f:
                f.write(iyang_model)

        build_py.run(self)

setup(
    author="lnos-coders",
    author_email='lnos-coders@linkedin.com',
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Package contains YANG models for sonic.",
    license="GNU General Public License v3",
    long_description=readme + '\n\n',
    install_requires = [
    ],
    tests_require = [
        'pytest',
        'ijson==2.6.1'
    ],
    setup_requires = [
        'pytest-runner',
        'wheel'
    ],
    include_package_data=True,
    keywords='sonic-yang-models',
    name='sonic-yang-models',
    py_modules=[],
    packages=find_packages(),
    version='1.0',
    cmdclass={'build_py': my_build_py},
    data_files=[
        ('yang-models', ['./yang-models/sonic-acl.yang',
                         './yang-models/sonic-bgp-common.yang',
                         './yang-models/sonic-bgp-global.yang',
                         './yang-models/sonic-bgp-neighbor.yang',
                         './yang-models/sonic-bgp-peergroup.yang',
                         './yang-models/sonic-breakout_cfg.yang',
                         './yang-models/sonic-copp.yang',
                         './yang-models/sonic-crm.yang',
                         './yang-models/sonic-device_metadata.yang',
                         './yang-models/sonic-device_neighbor.yang',
                         './yang-models/sonic-extension.yang',
                         './yang-models/sonic-flex_counter.yang',
                         './yang-models/sonic-interface.yang',
                         './yang-models/sonic-loopback-interface.yang',
                         './yang-models/sonic-mgmt_interface.yang',
                         './yang-models/sonic-mgmt_port.yang',
                         './yang-models/sonic-mgmt_vrf.yang',
                         './yang-models/sonic-ntp.yang',
                         './yang-models/sonic-nat.yang',
                         './yang-models/sonic-port.yang',
                         './yang-models/sonic-portchannel.yang',
                         './yang-models/sonic-route-common.yang',
                         './yang-models/sonic-route-map.yang',
                         './yang-models/sonic-routing-policy-sets.yang',
                         './yang-models/sonic-system-aaa.yang',
                         './yang-models/sonic-system-tacacs.yang',
                         './yang-models/sonic-types.yang',
                         './yang-models/sonic-versions.yang',
                         './yang-models/sonic-vlan.yang',
                         './yang-models/sonic-vrf.yang',
                         './yang-models/sonic_yang_tree']),
        ('iyang-models', ['./iyang-models/sonic-acl.yang',
                         './iyang-models/sonic-bgp-common.yang',
                         './iyang-models/sonic-bgp-global.yang',
                         './iyang-models/sonic-bgp-neighbor.yang',
                         './iyang-models/sonic-bgp-peergroup.yang',
                         './iyang-models/sonic-breakout_cfg.yang',
                         './iyang-models/sonic-copp.yang',
                         './iyang-models/sonic-crm.yang',
                         './iyang-models/sonic-device_metadata.yang',
                         './iyang-models/sonic-device_neighbor.yang',
                         './iyang-models/sonic-extension.yang',
                         './iyang-models/sonic-flex_counter.yang',
                         './iyang-models/sonic-interface.yang',
                         './iyang-models/sonic-loopback-interface.yang',
                         './iyang-models/sonic-mgmt_interface.yang',
                         './iyang-models/sonic-mgmt_port.yang',
                         './iyang-models/sonic-mgmt_vrf.yang',
                         './iyang-models/sonic-ntp.yang',
                         './iyang-models/sonic-nat.yang',
                         './iyang-models/sonic-port.yang',
                         './iyang-models/sonic-portchannel.yang',
                         './iyang-models/sonic-route-common.yang',
                         './iyang-models/sonic-route-map.yang',
                         './iyang-models/sonic-routing-policy-sets.yang',
                         './iyang-models/sonic-system-aaa.yang',
                         './iyang-models/sonic-system-tacacs.yang',
                         './iyang-models/sonic-types.yang',
                         './iyang-models/sonic-versions.yang',
                         './iyang-models/sonic-vlan.yang',
                         './iyang-models/sonic-vrf.yang',
                         './iyang-models/sonic_yang_tree']),

    ],
    zip_safe=False,
)
