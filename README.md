# Stack Buffer Overflow (BOF) Python Toolkit

This repository is for register and share my learning path for exploit Stack based Buffer Overflow (BOF) in vulnerable binaries, using Python scripts for each debugging step, and as basic introduction to the reverse engineering.

### About the Toolkit

This repository is for practice purposes only, so when I have time again I'll try to practice and update everything.

## Buffer Overflow Proof of Concepts (PoC) using the Python Toolkit

* Brainpan 1 - PoC: https://joshuaprovoste.com/stack-buffer-overflow-brainpan/
     1. Python scripts: https://github.com/JoshuaProvoste/Stack-Buffer-Overflow-Python-Toolkit/tree/main/brainpan
* Vulnserver - PoC: https://joshuaprovoste.com/stack-buffer-overflow-vulnserver/
     1. Python scripts: https://github.com/JoshuaProvoste/Stack-Buffer-Overflow-Python-Toolkit/tree/main/vulnserver
* Minishare - PoC: coming soon
     1. Python scripts: coming soon
* SLMail - PoC: coming soon
     1. Python scripts: coming soon

### About the Exploitation Context of the PoCs

* **Ubuntu LTS**: I used this stable version as host system OS with two virtual machines, using Oracle VM VirtualBox:
     1. Windows XP (victim)
     2. Kali Linux (attacker)
* **Windows XP x86**: I used this deprecated system OS for two simple reasons:
     1. Fast load as virtual machine
     2. Does not require security settings that must be disabled
     3. If you want work with Windows 10, **don't forget disable all security settings**
* **Kali Linux**: To be honest, I don't like Kali, but the reasons for their use:
     1. Preinstalled two versions of Python
     2. Msfvenom and other tools are necessary

## Python Toolkit of 8 Exploitation Steps

The Buffer Overflow exploitation process have multiple and different steps, so, for make the process easier, I was coded Python scripts for each step:

* 01-socker.py - **Basic socket communication** - (Spiking)
* 02-crasher.py - **Python loop to make a crash** - (Fuzzing)
* 03-verifier.py - **Verification of amount characters** - (Fuzzing)
* 04-eiper.py - **Find the Offset value**
* 05-controller.py - **Control the EIP overwrite**
* 06-badcharer.py - **Identification of bad characters**
* 07-calc.py - **Verification of shellcode functionality**
* 08-exploit.py - **Final exploit to get a reverse shell connection**

### Why 8 Steps

Anyone can say that they are more or less steps, but this 8 steps I think are necessary to learn and understand the Buffer Overflow process having a good base.

## About the Usage of the Python Toolkit

**Please, read all the following items before to try use the Python Toolkit**:

1. Feel free [to ping me](https://twitter.com/JoshuaProvoste)
2. Every binary file are different from each other; yes, you should expect any type of error using the Python toolkit trying to exploit BOF with other binaries.
3. All Python files of the Python Toolkit are templates of code.
4. I recommend learn Python programming before to use the Python Toolkit, only with this knowledge you should solve the problems about the items N°2 and N°3 of this list.

### Installation

The Python Toolkit does not require installation of external modules.

### Sandbox Usage

Please, use the Python Toolkit with the latest version of Kali Linux.

## Arguments of the Python Scripts

#### 01-socker.py - Basic socket communication
`python3 01-socker.py -ip 192.168.0.7 -sp 9999`

#### 02-crasher.py - Python loop to make a crash
`python3 02-crasher.py -ip 192.168.0.7 -sp 9999 -lt A`

#### 03-verifier.py - Verification of amount characters to make a crash
`python3 03-verifier.py -ip 192.168.0.7 -sp 9999 -lt A`

#### 04-eiper.py - Find the EIP value
`python3 04-eiper.py -ip 192.168.0.7 -sp 9999 -pt your_pattern_list`

#### 05-controller.py - Control the EIP overwrite
`python3 05-controller.py -ip 192.168.0.7 -sp 9999 -ep 2003 -lt C -sh 400`

#### 06-badcharer.py - Identification of bad characters for shellcoding
`python3 06-badcharer.py -ip 192.168.0.7 -sp 9999`

#### 07-calc.py - Verification of shellcode functionality
`python3 07-calc.py`

#### 08-exploit.py - Final exploit to get a reverse shell connection
`python3 08-exploit.py`

## Pending technical considerations

* Mathematical subtraction of data as best practice
* `while` loop for exploit writing (simplification)
* `struct` module for little-endian representation
* `pwntools` CTF framework

## Credits

All kudos for God and my family. Time is Gold. 🥊

## References

The following links are the public references of this repository:

* https://github.com/gh0x0st/Buffer_Overflow
* https://github.com/V1n1v131r4/OSCP-Buffer-Overflow
* https://github.com/johnjhacking/Buffer-Overflow-Guide
* https://ironhackers.es/es/tutoriales/preparacion-oscp-windows-buffer-overflow-writeup-de-brainpain-vulnhub-2/
* https://www.youtube.com/watch?v=eOoacS8tys8
