%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/jazzy/.*$
%global __requires_exclude_from ^/opt/ros/jazzy/.*$

Name:           ros-jazzy-aruco-opencv
Version:        4.2.0
Release:        2%{?dist}%{?release_suffix}
Summary:        ROS aruco_opencv package

License:        MIT
Source0:        %{name}-%{version}.tar.gz

Requires:       python%{python3_pkgversion}-numpy
Requires:       python3-img2pdf
Requires:       python3-opencv
Requires:       ros-jazzy-aruco-opencv-msgs
Requires:       ros-jazzy-cv-bridge
Requires:       ros-jazzy-image-transport
Requires:       ros-jazzy-rclcpp
Requires:       ros-jazzy-rclcpp-components
Requires:       ros-jazzy-rclcpp-lifecycle
Requires:       ros-jazzy-tf2-geometry-msgs
Requires:       ros-jazzy-tf2-ros
Requires:       yaml-cpp-devel
Requires:       ros-jazzy-ros-workspace
BuildRequires:  ros-jazzy-ament-cmake
BuildRequires:  ros-jazzy-aruco-opencv-msgs
BuildRequires:  ros-jazzy-cv-bridge
BuildRequires:  ros-jazzy-image-transport
BuildRequires:  ros-jazzy-rclcpp
BuildRequires:  ros-jazzy-rclcpp-components
BuildRequires:  ros-jazzy-rclcpp-lifecycle
BuildRequires:  ros-jazzy-tf2-geometry-msgs
BuildRequires:  ros-jazzy-tf2-ros
BuildRequires:  yaml-cpp-devel
BuildRequires:  ros-jazzy-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  ros-jazzy-ament-cmake-copyright
BuildRequires:  ros-jazzy-ament-cmake-cpplint
BuildRequires:  ros-jazzy-ament-cmake-lint-cmake
BuildRequires:  ros-jazzy-ament-cmake-uncrustify
BuildRequires:  ros-jazzy-ament-cmake-xmllint
BuildRequires:  ros-jazzy-ament-lint-auto
%endif

%description
ArUco marker detection using aruco module from OpenCV libraries.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jazzy/setup.sh" ]; then . "/opt/ros/jazzy/setup.sh"; fi
mkdir -p .obj-%{_target_platform} && cd .obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/jazzy" \
    -DAMENT_PREFIX_PATH="/opt/ros/jazzy" \
    -DCMAKE_PREFIX_PATH="/opt/ros/jazzy" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
%if !0%{?with_tests}
    -DBUILD_TESTING=OFF \
%endif
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jazzy/setup.sh" ]; then . "/opt/ros/jazzy/setup.sh"; fi
%make_install -C .obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C .obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jazzy/setup.sh" ]; then . "/opt/ros/jazzy/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C .obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/jazzy

%changelog
* Thu Apr 18 2024 Fictionlab <support@fictionlab.pl> - 4.2.0-2
- Autogenerated by Bloom

* Fri Apr 05 2024 Fictionlab <support@fictionlab.pl> - 4.2.0-1
- Autogenerated by Bloom

* Tue Mar 05 2024 Fictionlab <support@fictionlab.pl> - 4.1.1-2
- Autogenerated by Bloom

