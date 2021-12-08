MAKE = make
PROGRAMS = eumaclang tac2mips 

.PHONY: $(PROGRAMS)

all: $(PROGRAMS)

eumaclang:
	cd src/lang && $(MAKE) || \
	(echo -e "\n\033[1;31mError. \033[0mEumaclang compilation termined." && exit 1)
	mv src/lang/eumaclang bin/ 
	echo -e "\n\033[1;36mEumaclang compilation successfully.\033[0m"

tac2mips:
	cd src/tac && $(MAKE) || \
	(echo -e "\n\033[1;31mError. \033[0mTac2mips compilation termined." && exit 1)
	mv src/tac/tac2mips bin/ 
	echo -e "\n\033[1;36mTac2mips compilation successfully.\033[0m"

clean:
	rm ./bin/*
