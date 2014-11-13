VirtualMachine
==============
Written by [Claus Topholt](mailto:claus@topholt.com).

This is a demonstration of a simulated, distributed, stack-based microprocessor (a virtual machine) with a
hypothetical integer-only instruction set. Programs are written in a simple high-level language which supports
limited integer math, while-loops, if-else statements, comments and console output.

Each program's source code is compiled to bytecodes and placed into a 512-byte memory block, which the virtual
machine's "cpu" operates on. The "cpu" is actually distributed across a number of isolated worker processes,
which can scale across physical (or virtual) hardware. The memory blocks are stored in a central
[Redis](http://redis.io") cache and the worker threads periodically serialize and de-serialize the blocks in order to
execute code. All data from the virtual machine, such as memory, registers, disassembly and console output is streamed
back to the user with websockets using a pub/sub pattern.

The virtual machine is written in Python 2.7. The simple language uses the [ANTLR4](http://www.antlr.org") lexer/parser. The
website runs [Flask](http://flask.pocoo.org) on [gunicorn](http://gunicorn.org) and everything is hosted on
[DigitalOcean](http://www.digitalocean.com).

Please note: This is a toy project, used to examine various architectural ideas and patterns. It is
*not* a production-like implementation of a virtual machine. That said, you are welcome to clone the source code.

Pre-requisites (pip): enum34, antlr4-python2-runtime, redis and Flask.

##For a running demo and a more in-depth explanation, please visit [topholt.com](http://virtualmachine.topholt.com:5000).