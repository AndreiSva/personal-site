Sail VM is a work in progress stack based bytecode interpreter virtual machine for POSIX compliant operating systems built in pure C99. It aims to be simple, fast, and as portable as possible.

## Why C?
Although it would have been much easier to develop this project in another language such as C++ or Rust, it would have went against several of my main goals for this project.

* Every operating system built since 1980 has a POSIX compliant libc as well as at least one compliant C compiler. By using another language I would restrict the platforms my virtual machine would be able to run on.

* Languages like Rust offer more abstractions which make it less straight forward to implement low level functions

## Features

* 4x 32 bit registers (1, 2, 3 and 4)

* dynamically reallocated 32 bit stack

* 32 bit RAM memory
