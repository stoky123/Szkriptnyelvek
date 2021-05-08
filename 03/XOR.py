#!/usr/bin/env python3


def xor(var1, var2):
    return bool(var1) != bool(var2)


def main():
	if(xor(None,"python")):	
	    print("A két változó logikai értéke különböző.")
	else:
		print("A két változó logikai értéke megegyezik.")


##########################


if __name__ == "__main__":
    main()
