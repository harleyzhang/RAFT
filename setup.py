import setuptools
from distutils.core import setup, Extension
from torch.utils.cpp_extension import CUDAExtension, BuildExtension
#from pip.req import parse_requirements
import subprocess

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="raft", # End-to-end vedio compression
    version="0.0.1",
    author="",
    author_email="",
    description="Recurrent All Paris Field Transforms for Optical Flow",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: :: ",
        "Operating System :: OS Independent",
    ],

    #install_reqs = parse_requirements('Requirements.txt', session='hack'),

    #Extension modules for torchac
    ext_modules = [
      # torchac for arithmetic codec
      CUDAExtension(
        name='alt_cuda_corr',
        sources=['alt_cuda_corr/correlation.cpp', 'alt_cuda_corr/correlation_kernel.cu'],
        extra_compile_args={'cxx': [], 'nvcc': ['-O3']}),
    ],

    cmdclass = {
      'build_ext': BuildExtension
    },

    python_requires='>=3.7',
)
