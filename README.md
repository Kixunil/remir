# RemIR

A simple server for controlling IR-enabled devices.

## About

This is a very simple server written in Python using `bottle` framework that allows you
to control IR devices using `lirc`.

It's recommended to install it using [Cryptoanarchy Debian Repository](https://deb.ln-ask.me).

It auto-detects devices and buttons from LIRC, so it shouldn't require any configuration on top
of configuring LIRC itself.
