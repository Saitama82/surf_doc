.. _start_guide:


.. |clearfloat|  raw:: html

   <div class="clearer"></div>

*****************
Quick Start Guide
*****************

This chapter describes how you can quickly get started with the SURF platform. We show how to download
and install the SURF Virtual Machine and all the SURF packages. We describe how to compile (if needed) the source codes.
We present how to execute a case study (template) experiment in the Gulf of Taranto and view the results.
Finally we show how the user-configuration file of a template experiment can be modified in order to
execute and analysis new experiments.
The template experiment make it easier to run the model without a detailed knowledge of the underlying
scientific basis. Only a limited number of default values need to be changed for most applications.
A more specific scientific background is required if for example the user intends to perform experiments
with different turbulence or numerical schemes or with alternative settings of model parameters.
It is then recommended to read first the NEMO Model Description document and relative article.

See also the video tutorials available online `here <http://surf.local/tutorial.php>`_
explain basic features of the SURF platform and designed for beginners who want to learn SURF step by step.

Download and Install SURF Virtual Machine
=========================================

The SURF platform will be provide as a Virtual Machine (VM). It is packaged and distributed as a GZIP
Compressed Tar Archive file (tar.gz file suffix) which contains two VDI (VirtualBox Disk Image) files:

* ``surf.vdi`` for the operating system
* ``surf_scratch.vdi`` for source code files, datasets sample, and experiments.

The general scheme adopted to manage the versions provides that the releases contain in the name
indications of the version in the format:

.. code-block:: sh

   surf_vm_VERSION.tar.gz

where VERSION is a number (e.g. surf_vm\_\ |version_vm|.tar.gz for the current version). The instructions below
explain how to download, install and configure the SURF VM in Oracle VirtualBox



.. container:: twocol

   .. container:: leftside

      * Navigate to https://www.virtualbox.org/ and click on *Downloads* button.
        Choose the ``VirtualBox base package`` (version >=6) corresponding to the host
        operating system of your computer (i.e. Windows, Mac, Linux) and the additional
        ``Extension Packs`` which extend the functionality of the VirtualBox base package.
        Save the corresponding files on your computer then execute them and follow the
        installation instructions. Please install the same version extension pack
        as your installed version of VirtualBox.

   .. container:: rightside

      .. _fig-VM_install0:
      .. figure:: _static/figure/fig_install/VM_install0.png
         :width: 500px

         Downloads Virtual Box


   .. container:: leftside

      * Download the current version (v\ |version_vm|) of the SURF virtual machine from
        `SURF web-page <http://surf.local/download.php>`_ and extract it in your VirtualBox directory
        (``/Users/USERNAME/VirtualBox VM/`` for Mac user).
        tar -zxvf surf\_\ |version_vm|.tar.gz

        .. parsed-literal::

           tar -zxvf surf\_\ |version_vm|.tar.gz

        You need to create an account and log in to have access to downloads.

   .. container:: rightside

      .. _fig-VM_install1:
      .. figure:: _static/figure/fig_install/VM_install1.png
         :width: 500px

         Downloads SURF Virtual Machine


   .. container:: leftside

      * Open the VirtualBox software. From the menu, choose *Machine* > *add* and navigate to the .vbox file.
        This will add the Virtual Machine ``surf`` to the list of Virtual Machine

   .. container:: rightside

      .. _fig-VM_install2:
      .. figure:: _static/figure/fig_install/VM_install2.png
         :width: 500px

         Add SURF-VM in VirtualBox

   .. container:: leftside

      * To start the VM surf, you can double-click on its entry in the machines manager or select its entry
        and press the *Start* button on the top. A window opens.
        The VM Login should look like the right figure. In the login dialog box enter:

        * *surf* as login
        * *surf2019* as an initial password

        You are now logged into the VM.

   .. container:: rightside

      .. _fig-VM_install3:
      .. figure:: _static/figure/fig_install/VM_install3.png
         :width: 500px

         Add SURF-VM in VirtualBox




Changing Configuration on the SURF Virtual Machine
--------------------------------------------------

By default, the VM surf is configurated as in table :numref:`tab-configVM`. You can keep all defaults parameters or if it is not
adequate for your application you can change settings

.. container:: twocol

   .. container:: leftside

      * To change the configuration settings, you right-click the surf virtual machine’s name and choose *Setting*.
        You can change setting such as: (1) increase/decrease the number of cores based on your performance desires,
        (2) increase/decrease the number of GB of RAM allocated to your VM according to the size of you computational domain,
        (3) add a 2nd network adapter e.g. Host-Only adapter so that the Host can have direct connection with the Guest.

   .. container:: rightside

      .. _fig-VM_install4:
      .. figure:: _static/figure/fig_install/VM_install4.png
         :width: 500px

         Add SURF-VM in VirtualBox


   .. container:: leftside

      * Enlarge the virtual disk in order to storage more data.

        .. code-block:: sh

           VBoxManage modifyhd YOUR_HD.vdi
           –resize SIZE_MB

   .. container:: rightside

      .. _fig-VM_install5:
      .. figure:: _static/figure/fig_install/VM_install5.png
         :width: 500px

         Enlarge the virtual disk



.. _tab-configVM:
.. list-table:: Virtual Machine Summary Fields.
 :widths: 2 6 2
 :header-rows: 1

 * - Parameter
   - Description
   - Values
 * - Name
   - Name given the VM
   - surf
 * - Guest OS
   - Operating system running on this VM
   - Debian Linux
 * - Memory
   - Amount of memory available to this VM
   - 2 [GB]
 * - Cores
   - Number of CPU cores being used by this VM
   - 2
 * - Disk Capacity
   - Total disk capacity available to this VM
   - 40 [GB]
 * - Network Adapters
   - Number of network adapters available to this VM
   - 1
 * - IP Address
   - IP address assigned to the VM
   - x




Download and Install SURF packages
==================================

Once logged in, open a new terminal windows and go to the directory ``/scratch``. The scratch directory
follows the directory structure as shown in fig. xx. The VM you have installed does not contain the SURF
packages (source codes and datasets) and you need to download and install them. The SURF packages are
packaged and distributed as a GZIP Compressed Tar Archive file (tar.gz file suffix). The general scheme
adopted to manage the versions provides that the releases contain in the name indications of the version in
the format:

.. code-block:: sh

   packageName_VERSION.tar.gz

where VERSION is a number (e.g. surf_nemo\_\ |version_nemo|.tar.gz for the current version of the surf_nemo package).
The instructions below explain how to install the package in the VM:

* Once logged in the VM surf, download the current version of the SURF-NEMO (surf_nemo\_\ |version_nemo|.tar.gz)
  and SURF-DATASETS (surf_datasets\_\ |version_data|.tar.gz) packages directly from the
  `SURF web-page <https://surf.sincem.unibo.it>`_ and save it in the directory  ``/scratch/surf/surf_install/releases/``.

* Go to the directory ``/scratch/surf/surf_install/releases/`` and run the installation bash script
  ``install.sh`` followed by the package name. For the SURF-NEMO packages type:

  .. parsed-literal::

     install.sh surf_nemo\_\ |version_nemo|.tar.gz

  For the SURF-DATASETS packages type:

  .. parsed-literal::

     install.sh surf_datasets\_\ |version_data|.tar.gz

  The installation process will extract the archive in the directory ``/scratch/surf/surf_nemo/`` and
  ``/scratch/surf/surf_datasets/``, respectively, and will create a symbolic link current in this directory
  that points to the extracted folder.

For a detailed description of the directory structure and contents of each packages refer to the Appendix A.


Compiling the source code
=========================

After the installation of the SURF-NEMO package is finished, you need to compile the source codes in order
to create the executable files needed to perform specific tasks. The executable files should not be recreated
unless you need to modified the source code. Compilation is performed with the Unix/Linux make utility
using the following tools: (1) fortran 90 compiler, (2) C-preprocessor cpp, (3) a compiled MPI library for
simulations in parallel mode. (4) a compiled netCDF library to read and write data in portable netCDF
format. All these tools are already present and compiled in the SURF platform.

To compile the source codes go to the directory ``/scratch/surf/surf_nemo/current/scripts/`` and run
the compilation bash script ``compile.sh`` followed by the package name (or by the word ’all’ to compile
all the packages):

.. code-block:: sh

   cd /scratch/surf/surf_nemo/current/scripts ; ./compile_codes.sh all

Compilation could take a few minutes and it will create the executable files for each program present in the
SURF-NEMO package.



Running the case study: Gulf of Taranto
=======================================

As case study we implement the SURF platform in the Gulf of Taranto in the northern Ionian Sea (fig xx).
The nesting simulation start on 5 October 2014 at 00:00 and run until 7 October 2014 at 24:00.
In order to execute this case study experiment, you can follow these steps:

* Download the input datasets (gulfTaranto_20141005.tar.gz) of this case study directly from the web-repository
  (https://surf.sincem.unibo.it) and extract it in the directory ``/scratch/surf/indata_offline/``

  .. code-block:: sh

     tar -zxvf gulfTaranto_20141005.tar.gz

  Note If you want to change the local repository path to some other location of your choice make sure to change the path in the configuration file.

* Create a new folder in the directory ``/scratch/from_GUI/`` and let’s call it gulfTaranto_20141005.
  This is the Experiment ID name which uniquely identifies the experiment.

  .. code-block:: sh

     cd /scratch/from_GUI/ ; mkdir gulfTaranto_20141005

* Copy the template configuration file ``/scratch/surf/surf_nemo/current/setParFree.json`` in the
  directory ``/scratch/from_GUI/gulfTaranto_20141005/`` which contains the configuration for this case study.

  .. code-block:: sh

  	  necd ; cp setParFree.json /scratch/from_GUI/gulfTaranto_20141005/

* After that, from the directory /scratch/surf/surf_nemo/current/scripts/, you just need to execute
  the julia script run_exp.jl followed by the experiment ID ``gulfTaranto_20141005``

  .. code-block:: html

     julia run_exp.jl gulfTaranto_20141005

  This will create the folder gulfTaranto_20141005 in the directory ``/scratch/surf/experiments/``
  with a directory tree as in fig.x.1 (refer to the Appendix x for more details)

You can activate/deactivate specific tasks by setting logical parameters to True/False
in the section ``set_lrun`` of the configuration file ``setParFree.json``

.. container:: twocol

   .. container:: leftside

      ``lrun_childMeshmask`` to  enable the execution of the CHILD-MESHMASK GENERATION task.

      ``lrun_regridPreAtm`` to enable the execution of the ATMOSPHERIC-DATA-REGRIDDING task.

      ``lrun_regridPreOceIC`` to enable the execution of the OCEAN-IC-DATA-REGRIDDING task.

      ``lrun_regridPreOceBC`` to enable the execution of the OCEAN-BC-DATA-REGRIDDING task.

      ``lrun_regridPreWeights`` if you want to compute (=True) or just copy (=False) the WEIGHT-FILEs for REMAPPING in the Regridding phase.

      ``lrun_ocean`` to enable the execution of the NEMO code.

   .. container:: rightside

      .. code-block:: JSON
         :name: json_set_lrun
         :caption: user-configuration file section set_lrun

         {"id":"A001","title":"set_lrun",
            "items": [
               {"name": "lrun_childMeshMask",
                "value": "True"
               },
               {"name": "lrun_regridPreAtm",
                "value": "True"
               },
               {"name": "lrun_regridPreOceIC",
                "value": "True"
               },
               {"name": "lrun_regridPreOceBC",
                "value": "True"
               },
               {"name": "lrun_regridPreWeights",
                "value": "True"
               },
               {"name": "lrun_ocean",
                "value": "True"
               }
            ]
         }

|clearfloat|


Post-processing the results
===========================

The surf package is provided together with open source tools for data visualization and post-processing your data.
You will find the free software packages NcView with graphical user interface
and a suite of procedure using NCAR Graphics package with NCL and Python interface you can call from Command Line.

However, it is very well possible to use other (free or commercial)
graphic software such as Pynoply or several scripting languages such as julia, IDL, Matlab, as long
as they can read the netCDF format.

Visualizing the results with Ncview
-----------------------------------

Ncview is a tool for visualizing netCDF data files. It is very easy to use, because of its graphical user interface.
However, its possibilities are limited. Typically you would use ncview to get a quick and easy, push-button
look at your netCDF files. You can view simple movies of the data, view along various dimensions, take a
look at the actual data values, change color maps, invert the data, etc.
In order to start this program type ncview followed by the filename of the dataset you want to visualize,
example type the following command

.. code-block:: sh

   ncview SURF_1h_20141006_20141006_grid_T.nc

An example of the user interface in NcView is given in figure :numref:`fig-ncview`


.. _fig-ncview:
.. figure:: _static/figure/fig_testcase/ncview.png
   :width: 50%

   This is the caption of the figure.

Analyzing and Visualizing results using NCAR graphic packages
-------------------------------------------------------------

NCAR Graphics is a collection of graphics libraries that support the display of scientific data. One possible
interfaces available for visualizing data with these libraries is with the NCAR Command Language (NCL),
an open source interpreted programming language, developed at NCAR and designed for the analysis and
visualization of geoscientific data.

The SURF-NEMO package include, as postprocessing, a suite of NCL functions to visualize the input/output
datasets, compare the child/parent fields, compare the simulation result with insitu or satellite datasets and
convert datasets.

.. list-table::

 * - .. _fig-test1_velxy:
     .. figure:: _static/figure/fig_testcase/velxy_z000_t035.png

        This is the caption of the figure.

   - .. _fig-test1_tempxy:
     .. figure:: _static/figure/fig_testcase/tempxy_z000_t035.png

        This is the caption of the figure.

   - .. _fig-test1_tempxz:
     .. figure:: _static/figure/fig_testcase/tempxz_y000_t035.png

        This is the caption of the figure.

In order to Post-processing the results of an existing experiment, you need to execute the julia script
``run_postProc.jl`` followed by the experiment ID. Example for the case study experiment type the following
command:

.. code-block:: sh

   julia run_postproc.jl gulfTaranto_20141005


You can activate/deactivate specific tasks by setting logical parameters to True/False
in the sections ``set_lrun_post`` and ``set_visual_lplot`` of the configuration file ``setParFree.json``

.. container:: twocol

   .. container:: leftside

      ``lrun_visDom`` to  enable the plotting of the user defined Domains.

      ``lrun_visIndata`` to  enable the plotting of the Indata Bat,Atm,OceIC,OceBC fields.

      ``lrun_visExtrapdata`` to enable the plotting of the Extrapdata Atm,OceIC,OceBC fields.

      ``lrun_visRegriddata`` to enable the execution of the OCEAN-IC-DATA-REGRIDDING task.

      ``lrun_visOutdata`` to enable the execution of the OCEAN-BC-DATA-REGRIDDING task.

      ``lrun_chlVSpar`` if you want to compute (=True) or just copy (=False) the WEIGHT-FILEs for REMAPPING in the Regridding phase.

      ``lrun_surfVSctd`` enables the execution of the NEMO code.

      ``lrun_surfVSsat`` enables the execution of the NEMO code.

      ``lrun_surfVSmooring`` enables the execution of the NEMO code.

      ``lrun_surfVSferrybox`` enables the execution of the NEMO code.

   .. container:: rightside

      .. code-block:: JSON
         :name: json_set_lrun_post
         :caption: user-configuration file section set_lrun_post

         {"id":"B000","title":"set_lrun_post",
            "items": [
                {"name": "lrun_visDom",
                 "value": "True"
                },
                {"name": "lrun_visIndata",
                 "value": "True"
                },
                {"name": "lrun_visExtrapdata",
                 "value": "True"
                },
                {"name": "lrun_visRegriddata",
                 "value": "True"
                },
                {"name": "lrun_visOutdata",
                 "value ": "True"
                },
                {"name": "lrun_chlVSpar",
                 "value": "True"
                },
                {"name": "lrun_surfVSctd",
                 "value": "True"
                },
                {"name": "lrun_surfVSsat",
                 "value": "True"
                },
                {"name": "lrun_surfVSmooring",
                 "value": "True"
                },
                {"name": "lrun_surfVSferrybox",
                 "value": "True"
                }
             ]
         }

|clearfloat|



.. container:: twocol

   .. container:: leftside

      ``lplotMesh`` to  enable plotting of the Child MeshMask fields.

      ``lplotBat`` to enable the plotting of the Bathymetry fields.

      ``lplotAtm`` to enable the plotting of the Atmspheric fields.

      ``lplotOceIC`` to enable the plotting of the Initial Condition Ocean fields.

      ``lplotOceBC`` to enable the plotting of the Open Boundary Condition Ocean fields.

      ``lplotOceBCbdy`` to enable the plotting of the Open Boundary Condition Ocean fields.

      ``lplotOceOut`` to enable the plotting of the Output Ocean fields.

   .. container:: rightside

      .. code-block:: JSON
         :name: json_set_visual_lplot
         :caption: user-configuration file section set_visual_lplot

         {"id":"B001","title":"set_visual_lplot",
           "items": [
               {"name": "lplotMesh",
                "value": "True"
               },
               {"name": "lplotBat",
                "value": "True"
               },
               {"name": "lplotAtm",
                "value": "True"
               },
               {"name": "lplotOceIC",
                "value ": "True"
               },
               {"name": "lplotOceBC",
                "value": "True"
               },
               {"name": "lplotOceBCbdy",
                "value": "True"
               },
               {"name": "lplotOceOut",
                "value": "True"
               }
            ]
         }

|clearfloat|


Make a new experiments
----------------------

Let's assume you want to study the circulation of the Sermilik fjord in Greenland
from 1 February 2017 at 00:00 to 7 February 2017 at 24:00.... add more details.

* Choose the name of experiment ID (e.g. ``greenlandFjord_20170201``) and create the folder

  .. code-block:: html

     cd /scratch/from_GUI/ ; mkdir greenlandFjord_20170201

* Copy the template configuration file ``/scratch/surf/surf_nemo/current/setParFree.json`` in the
  directory ``/scratch/from_GUI/greenlandFjord_20170201``

  .. code-block:: html

     cp /scratch/surf/surf_nemo/current/setParFree.json ./greenlandFjord_20170201/

* Modify the user configuration file ``setParFree.json`` according to your needs

  .. code-block:: html

     param1 = xxx
     param2 = xxx
     param3 = xxx
     param4 = xxx

* From the directory ``/scratch/surf/surf_nemo/current/scripts/``, execute
  the julia script ``run_exp.jl`` followed by the experiment ID ``greenlandFjord_20170201``

  .. code-block:: html

     cd /scratch/surf/surf_nemo/current/scripts/ ;
     julia run_exp.jl greenlandFjord_20170201

* After running the simulation, you can display the simulation results by using
  the julia script ``run_postproc.jl`` followed by the experiment ID ``greenlandFjord_20170201``

  .. code-block:: html

     julia run_postproc.jl greenlandFjord_20170201

In principle you can simply use the template model and modify it to your needs, and not be too much
concerned with the input files they create. But our advice is never to use the template model as black boxes.
It is therefore important to understand how the codes work, which options they have and how their input
files are structured.


Multiple downscaling experiments
--------------------------------

Surf-nemo package includes multiple nesting capability
(i.e. consecutive nested models can be implemented with increasing grid resolutions).
Let's assume you want to downscaling from an existing experiment (e.g. from the template experiment
``gulfTaranto_20141005``) in order to increase the spatial resolution to 800m ... add details.

* Go to the existing experiment directory

  .. code-block:: html

     cd /scratch/surf/experiments/gulfTaranto_20141005/

* Modify the user configuration file ``setParFree.json`` according to your needs

  .. code-block:: html

     param1 = xxx
     param2 = xxx
     param3 = xxx
     param4 = xxx

* From the directory ``/scratch/surf/experiments/gulfTaranto_20141005/code/ocean/scripts/``, execute
  the julia script ``run_exp.jl`` followed by the experiment ID ``gulfTaranto_20141005``

  .. code-block:: html

     cd /scratch/surf/experiments/gulfTaranto_20141005/code/ocean/scripts/ ;
     julia run_exp.jl gulfTaranto_20141005

* After running the simulation, you can display the simulation results by using
  the julia script ``run_postproc.jl`` followed by the experiment ID ``gulfTaranto_20141005``

  .. code-block:: html

     julia run_postproc.jl gulfTaranto_20141005
