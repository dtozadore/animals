# CMake generated Testfile for 
# Source directory: /home/dtozadore/Projects/NaoPyTest/foo
# Build directory: /home/dtozadore/Projects/NaoPyTest/foo/build-sys-linux-x86_64
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(test_foo "/home/dtozadore/Projects/NaoPyTest/foo/build-sys-linux-x86_64/sdk/bin/test_foo")
set_tests_properties(test_foo PROPERTIES  TIMEOUT "20")
