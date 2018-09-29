#!/usr/bin/env python
# coding: utf-8
import sys
import platform

SIZE_ADRESS_64 = 8
SIZE_ADRESS_32 = 4

# Init e_ident const
ELF = bytearray([0x7f, 0x45, 0x4c, 0x46]) # .ELF

# EI_CLASS
ELFCLASSNONE = bytearray([0x00]) # Invalid class
ELFCLASS32 = bytearray([0x01]) # 32-bit object
ELFCLASS64 = bytearray([0x02]) # 64-bit object

# EI_DATA
ELFDATANONE = bytearray([0x00]) # Invalid data encoding
ELFDATA2LSB = bytearray([0x01]) # LSB
ELFDATA2MSB = bytearray([0x02]) # MSB

# EI_VERSION
EV_NONE = bytearray([0x00]) # Invalid version
EV_CURRENT = bytearray([0x01]) # Current version

# EI_PAD
EI_PAD = bytearray([0x00]*9)

# Init e_type
ET_NONE = bytearray([0x00, 0x00]) # No file type
ET_REL = bytearray([0x01, 0x00]) # Relocatable file
ET_EXEC = bytearray([0x02, 0x00]) # Executable file
ET_DYN = bytearray([0x03, 0x00]) # Shared object file
ET_CORE = bytearray([0x04, 0x00]) # Core file
ET_LOPROC = bytearray([0xff, 0x00]) # Processor-specific
ET_HIPROC = bytearray([0xff, 0xff]) # Processor-specific

# Init e_machine conf
EM_NONE = bytearray([0x00]) # No machine
EM_M32 = bytearray([0x01]) # AT&T WE 32100
EM_SPARC = bytearray([0x02]) # SPARC
EM_386 = bytearray([0x03]) # Intel 80386
EM_68K = bytearray([0x04]) # Motorola 68000
EM_88K = bytearray([0x05]) # Motorola 88000
EM_860 = bytearray([0x07]) # Intel 80860
EM_MIPS = bytearray([0x08]) # MIPS RS3000
EM_POWERPC = bytearray([0x14]) # PowerPC
EM_S390 = bytearray([0x16]) # S390
EM_ARM = bytearray([0x28]) # ARM
EM_SUPERH = bytearray([0x2A]) # SuperH
EM_IA_64 = bytearray([0x32]) # IA-64
EM_X86_64 = bytearray([0x3E, 0x00]) # x86-64
EM_AARCH64 = bytearray([0xB7]) # AArch64
EM_RISC_V = bytearray([0xF3]) # RISC-V

if __name__ == "__main__":
    arch, exe_type = platform.architecture()
    is_linux = platform.system() == "Linux"
    is_elf = exe_type == "ELF"
    is_64, is_32 = arch == "64bit", arch == "32bit"
    is_x86_64 = platform.machine() == "x86_64"
    with open("result", "wb") as outfile:
        if is_elf:
            # Заполняем заголовки исполняемого файла
            # ***************e_ident***************
            fileheader = ELF
            if is_64:
                fileheader += ELFCLASS64
            elif is_32:
                fileheader += ELFCLASS32
            else:
                fileheader += ELFCLASSNONE
            fileheader += ELFDATA2LSB
            fileheader += EV_CURRENT
            fileheader += EI_PAD

            # ***************e_type***************
            fileheader += ET_EXEC

            # ***************e_machine***************
            if is_x86_64:
                fileheader += EM_X86_64
            else:
                fileheader += EM_NONE

            # ***************e_version***************
            fileheader += EV_CURRENT + bytearray([0x00, 0x00, 0x00])

            # ***************e_entry***************
            if is_64:
                fileheader += bytearray([0x00]*SIZE_ADRESS_64)
            elif is_32:
                fileheader += bytearray([0x00]*SIZE_ADRESS_32)

            # ***************e_phoff***************
            if is_64:
                fileheader += bytearray([0x40]) + bytearray([0x00]*(SIZE_ADRESS_64-1))
            elif is_32:
                fileheader += bytearray([0x34]) + bytearray([0x00]*(SIZE_ADRESS_32-1))

            # ***************e_shoff***************
            if is_64:
                fileheader += bytearray([0x00]*SIZE_ADRESS_64)
            elif is_32:
                fileheader += bytearray([0x00]*SIZE_ADRESS_32)

            # Заполняем таблицы
            outfile.write(fileheader)
