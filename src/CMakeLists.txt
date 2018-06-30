cmake_minimum_required(VERSION 2.8)
project(Sometimes CXX)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

add_library(sometimes sometimes.cpp)
target_link_libraries(sometimes CONAN_PKG::boost_date_time)
