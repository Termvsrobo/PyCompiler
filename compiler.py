#!/usr/bin/env python

if __name__ == "__main__":
	with open("result", "wb") as outfile:
		fileheader = bytearray([0x7f, 0x45, 0x4c, 0x46]) # .ELF
		fileheader.append(0x02) # EI_CLASS 
		fileheader.append(0x01) # EI_DATA
		fileheader.append(0x01) # EI_VERSION
		fileheader + bytearray([0x00]*9)
		outfile.write(fileheader)
