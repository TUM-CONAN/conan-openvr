# Conan package of OpenVR

[![Download](https://api.bintray.com/packages/arsen-studio/arsen-deps/openvr%3Aarsen-studio/images/download.svg?version=1.0.14%3Astable)](https://bintray.com/arsen-studio/arsen-deps/openvr%3Aarsen-studio/1.0.14%3Astable/link)

|Linux|Windows|OS X|
|-----|-------|----|
|[![pipeline status](https://gitlab.com/HeiGameStudio/ArsenEngine/dependencies/conan-openvr/badges/stable/1.0.14/pipeline.svg)](https://gitlab.com/HeiGameStudio/ArsenEngine/dependencies/conan-openvr/commits/stable/1.0.14)|[![Build status](https://ci.appveyor.com/api/projects/status/qg7k3dywc13q7k6i/branch/stable%2F1.0.14?svg=true)](https://ci.appveyor.com/project/ArsenStudio/conan-openvr/branch/stable%2F1.0.14)|[![Build Status](https://travis-ci.org/ArsenStudio/conan-openvr.svg?branch=stable%2F1.0.14)](https://travis-ci.org/ArsenStudio/conan-openvr)|

[Conan.io](https://conan.io) package for [OpenVR](https://github.com/ValveSoftware/openvr) SDK.

The packages generated with this **conanfile** can be found in [bintray.com](https://bintray.com/arsen-studio/arsen-deps/openvr%3Aarsen-studio).

## Setup

To configure Conan client to work with Arsen packages, you will need to add repository to the list of remotes. To add repository, use the following command:

```sh
conan remote add arsen-deps https://api.bintray.com/conan/arsen-studio/arsen-deps
```

### Basic

```sh
conan install openvr/1.0.14@arsen-studio/stable
```

### Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*

```ini
[requires]
openvr/1.0.14@arsen-studio/stable

[options]
openvr:shared=true # false

[generators]
txt
cmake
```

Complete the installation of requirements for your project running:

```sh
conan install .
```

Project setup installs the library (and all his dependencies) and generates the files *conanbuildinfo.txt* and *conanbuildinfo.cmake* with all the paths and variables that you need to link with your dependencies.

## Develop the package

### Build packages

```sh
pip install conan_package_tools bincrafters_package_tools
python build.py
```

### Upload packages to server

```sh
conan upload openvr/1.0.14@arsen-studio/stable --all
```

## Issues

If you wish to report an issue, please do so here:

<https://gitlab.com/ArsenStudio/ArsenEngine/dependencies/conan-openvr/issues>

For any pull or merge request, please do so here:

<https://gitlab.com/ArsenStudio/ArsenEngine/dependencies/conan-openvr/merge_requests>

## License

[MIT LICENSE](LICENSE)
