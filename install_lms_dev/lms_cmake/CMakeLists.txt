add_subdirectory(/home/phibedy/Documents/programming/c++/lms/lms_tools/install_lms_dev/dependencies/lib1)
add_subdirectory(/home/phibedy/Documents/programming/c++/lms/lms_tools/install_lms_dev/dependencies/lib2)
add_subdirectory(/home/phibedy/Documents/programming/c++/lms/lms_tools/install_lms_dev/dependencies/package1)


file(GLOB toInclude *.cmake)
foreach(myPath ${toInclude})
    include(${myPath})
endforeach(myPath)