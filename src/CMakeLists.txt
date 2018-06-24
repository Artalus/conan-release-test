cmake_minimum_required(VERSION 2.8)
project(MyHello CXX)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

add_library(hello hello.cpp)
target_link_libraries(hello CONAN_PKG::boost_date_time)
