#!/usr/bin/env python

if __name__ == "__main__":
	with open("result", "wb") as outfile:
		fileheader = bytearray([0x7f, 0x45, 0x4c, 0x46])
		outfile.write(fileheader)
