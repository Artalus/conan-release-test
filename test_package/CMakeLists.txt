cmake_minimum_required(VERSION 2.8.12)
project(PackageTest CXX)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_executable(sometimesTest sometimesTest.cpp)
target_link_libraries(sometimesTest ${CONAN_LIBS})

# CTest is a testing tool that can be used to test your project.
# enable_testing()
# add_test(NAME sometimes
#          WORKING_DIRECTORY ${CMAKE_BINARY_DIR}/bin
#          COMMAND sometimes)
