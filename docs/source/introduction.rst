.. _introduction:

************
Introduction
************

The :github:`_url_` url is aliased to :github:`GitHub` and also to :github:`this`

The Structured and Unstructured grid Relocatable ocean platform for Forcasting (SURF) is an open source
package devoted to generate high resolution oceanic forecasts over limited domains of interest. It is designed
to be set up by non-expert users anywhere in the World Ocean with few steps and it is able to provide
timely (i.e. in near-real time) accurate forecasts even on a commercially available Personal Computer or a
laptop.

This User Guide describes the overall design of the up-to-date version release of the structured grid component of the SURF platform based on NEMO ocean model (https://www.nemo-ocean.eu). In addition to step-by-step information about running the SURF platform, the User Guide gives a detailed description
of the scripts organization and the data structures so that SURF can be modified/integrated by users as mandated by their particular research requirements. This User Guide gives also a case study experiment
using available input datasets for the bathymetry, the coastline, the atmospheric forcing and the coarser resolution parent ocean model and the output datasets to check the correct implementation of the software.

The information about the SURF numerical platform is online also at the home page

https://surf.sincem.unibo.it

Please see the lists of SURF publications and applications at that page.

.. _installing-docdir:

Relocatable ocean modelling system
==================================

The Structured and Unstructured Relocatable ocean model for Forecasting (SURF; Trotta et al. 2016)
provides a numerical platform for forecasting of hydrodynamic and thermodynamic fields at high spatial
and temporal resolutions. SURF is designed to be embedded in any region of a larger scale ocean prediction
system, at coarser resolution, and includes multiple nesting capabilities (i.e. consecutive nested models can
be implemented with increasing grid resolutions), starting with the first nesting in the large-scale ocean
model and reaching horizontal grid resolutions of a few hundred metres. For each nesting, the parent
coarse-grid model provides initial and lateral boundary conditions for the SURF child components.

This relocatable ocean model system aims to be a valuable tool in support to any Decision Support System
(DSS) which might need hydrodynamic, temperature and salinity forecasts, such as oil spill monitoring,
search and rescue operations, navigation routing, fisheries and tourism.

Virtual Machine Environment
===========================

SURF is working on a virtual machine environment where the hydrodynamic NEMO model and several pre- and post-processing tools are connected to the numerical outputs and the required inputs fields. Also
a non-virtual machine is suitable to run SURF since the user can access to the source code and executable.
See the Installation chapter 6.1.1 for how to download and install the package.

A virtual machine is a software-based computer that allow you to emulate additional operating systems
with "virtual" access to hardware resources such as CPU, RAM, networking and storage. The operating
system that runs inside a virtual machine is called the guest which appears in a window on your computer’s
operating system, commonly referred to as the *host*.

As virtualization software we use the free and open-source Oracle VM VirtualBox package where we install
the Debian Linux operating system.

Virtual machines offer many advantages and can encapsulate an entire PC environment including the operating
system, applications and all data inside a single file. Instead of installing a full bunch of softwares
working together it is therefore easier to set once a packaged application. Virtual machine can be distributed
as a ready-made fully configured system. A virtual machine provides advantages for configuration
and distribution. Furthermore a virtual machine can be executed on various hardware platforms.


Source Code
===========

The SURF source codes are contained in a package that is distributed as tar.gz archive. The archive
contains the NEMO code, the pre- and post-processing codes and a template user-configuration file. See
the Installation chapter 6.3 for how to download and install the package.

NEMO is an open source code written in Fortran 90 and is parallelized with a domain decomposition using
MPI library. All outputs are done with the NetCDF library.

The pre- and post-processing code are developed in Julia, NCL (NCAR Command Language) and Fortran
programming languages. NCO (NetCDF Operator) and CDO (Climate Data Operators) operators are also
used to facilitate manipulation of NetCDF datasets. These tools are specifically developed and optimised
for SURF in order to reduce the latency of the computation and to have efficient memory usage. For the
time being the pre- and post-processing can be run only in serial mode (i.e. can only be executed on one
processor). The structure of the SURF sorce code package is shown in chapter A.
