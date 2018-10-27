import os
from conans import ConanFile, CMake, tools


class OpenvrConan(ConanFile):
    name = "openvr"
    version = "1.0.14"
    description = ("API and runtime that allows access to VR hardware from"
                   "applications have specific knowledge of the hardware they are targeting."
                   "multiple vendors without requiring that "
                   "applications have specific knowledge of the hardware they"
                   "are targeting.")
    url = "https://gitlab.com/ArsenStudio/ArsenEngine/dependencies/conan-{0}".format(name)
    homepage = "https://github.com/ValveSoftware/openvr"

    license = "BSD 3-Clause"

    exports = ["LICENSE.md", "patch/*"]

    exports_sources = ["CMakeLists.txt"]
    generators = "cmake"

    settings = "os", "arch", "compiler", "build_type"
    options = {"shared": [True, False]}
    default_options = "shared=False"

    branch = ("v" if version != "master" else "") + version

    def source(self):
        source_url = "https://github.com/ValveSoftware/openvr"
        tools.get("{0}/archive/{1}.tar.gz".format(source_url, self.branch))
        extracted_dir = self.name + "-" + self.version

        os.rename(extracted_dir, "openvr")

        tools.replace_in_file("openvr/CMakeLists.txt", "project(OpenVRSDK)",
        '''project(OpenVRSDK)
           include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
           conan_basic_setup()''')

        # https://github.com/ValveSoftware/openvr/issues/364
        # https://github.com/ValveSoftware/openvr/pull/483
        if self.settings.compiler == "Visual Studio":
            tools.patch(base_path="openvr", patch_file="patch/openvr.h.patch")
            tools.patch(base_path="openvr", patch_file="patch/CMakeLists.txt.patch")

    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.configure(source_folder="openvr", defs={
            "BUILD_SHARED": self.options.shared,
            "USE_LIBCXX": self.settings.compiler != "Visual Studio" and str(self.settings.compiler.libcxx) == "libc++"
        })
        return cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        cmake = self._configure_cmake()
        cmake.install()
        self.copy("*.h", dst="include", src="openvr/headers")
        self.copy(pattern="openvr_api*.dll", dst="bin", src="bin", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)

        if self.settings.os == "Macos":
            self.cpp_info.exelinkflags.append("-framework Foundation")
            self.cpp_info.sharedlinkflags = self.cpp_info.exelinkflags

        if self.settings.os != "Windows":
            self.cpp_info.libs.append("dl")
